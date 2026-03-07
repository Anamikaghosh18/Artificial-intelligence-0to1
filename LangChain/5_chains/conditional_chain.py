from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableBranch
from pydantic import BaseModel, Field
from typing import Literal
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

# -----------------------------
# 1️⃣ Define model
# -----------------------------
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="conversational",
    huggingfacehub_api_token=api_key
)
model = ChatHuggingFace(llm=llm)

# -----------------------------
# 2️⃣ Pydantic schema & parser
# -----------------------------
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Classify the sentiment of the feedback")

parser = PydanticOutputParser(pydantic_object=Feedback)

# -----------------------------
# 3️⃣ Sentiment classification prompt
# -----------------------------
sentiment_prompt = PromptTemplate(
    template=(
        "Classify the sentiment of the user feedback as either 'positive' or 'negative'.\n\n"
        "Feedback: {feedback}\n\n"
        "{format_instruction}"
    ),
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

sentiment_chain = LLMChain(
    llm=model,
    prompt=sentiment_prompt,
    output_parser=parser,
    output_key="sentiment",
    verbose=True
)

# -----------------------------
# 4️⃣ Define positive & negative feedback response chains
# -----------------------------
positive_prompt = PromptTemplate(
    template="Write a kind and appreciative response for a positive user feedback:\n\n{feedback}",
    input_variables=["feedback"]
)

negative_prompt = PromptTemplate(
    template="Write a polite and empathetic response for a negative user feedback:\n\n{feedback}",
    input_variables=["feedback"]
)

positive_chain = LLMChain(llm=model, prompt=positive_prompt, verbose=True)
negative_chain = LLMChain(llm=model, prompt=negative_prompt, verbose=True)

# -----------------------------
# 5️⃣ Define branch logic
# -----------------------------
branch_chain = RunnableBranch(
    (lambda x: x["sentiment"] == "positive", positive_chain),
    (lambda x: x["sentiment"] == "negative", negative_chain),
    default=negative_chain  # fallback if something unexpected happens
)

# -----------------------------
# 6️⃣ Combine: first classify, then branch
# -----------------------------
from langchain.schema.runnable import RunnableSequence

final_chain = RunnableSequence(first=sentiment_chain, last=branch_chain)

# -----------------------------
# 7️⃣ Run
# -----------------------------
feedback_input = input("Give the feedback: ")

result = final_chain.invoke({"feedback": feedback_input})

print("\n--- Final Response ---\n")
print(result)
