from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
import os 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser , ResponseSchema



load_dotenv()
api_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN")


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="conversational",
    huggingfacehub_api_token=api_key
)


model = ChatHuggingFace(llm = llm)

schema = [
    
    ResponseSchema(name = "fact_1", description = "Fact 1 about the topic"),
    ResponseSchema(name = "fact_2", description = "Fact 2 about the topic"),
    ResponseSchema(name = "fact_3", description = "Fact 2 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)


# 1st prompt -> detailed report 
template1 = PromptTemplate(
    template = "Give me the fact about {topic} \n{format_instruction}", 
    input_variables=['topic'], 
    partial_variables={"format_instruction" : parser.get_format_instructions()}
) 

chain = template1 | model | parser
respond = chain.invoke({"topic":"black hole"}) # need to send something so blank dict bcz no input is there 
print(respond)


