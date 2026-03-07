from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

# ----- Models -----
llm1 = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="conversational",
    huggingfacehub_api_token=api_key
)
model1 = ChatHuggingFace(llm=llm1)

llm2 = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="conversational",
    huggingfacehub_api_token=api_key
)
model2 = ChatHuggingFace(llm=llm2)

parser = StrOutputParser()

# ----- Prompts -----
prompt1 = PromptTemplate(
    template="Generate short notes for the given {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate short quiz-type questions and answers from the given {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document.\nNotes:\n{notes}\nQuiz:\n{quiz}",
    input_variables=["notes", "quiz"]
)

# ----- Chains -----
chain1 = LLMChain(
    llm=model1,
    prompt=prompt1,
    output_parser=parser,
    output_key="notes",
    verbose=True
)

chain2 = LLMChain(
    llm=model2,
    prompt=prompt2,
    output_parser=parser,
    output_key="quiz",
    verbose=True
)

# Run both in parallel
parallel_chain = RunnableParallel(
    notes=chain1,
    quiz=chain2
)

# Merge both outputs
merge_chain = LLMChain(
    llm=model1,
    prompt=prompt3,
    output_parser=parser,
    verbose=True
)

# ----- Execute -----
text_input = "The process of photosynthesis in plants"

# First: generate notes + quiz in parallel
results = parallel_chain.invoke({"text": text_input})

# Then: merge both outputs
final_output = merge_chain.invoke(results)

print("\n--- Final Combined Output ---\n")
print(final_output)


