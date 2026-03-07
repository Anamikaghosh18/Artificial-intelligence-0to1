# single chat message using dynamic template 

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import load_prompt
import os
from dotenv import load_dotenv
import streamlit as st 


load_dotenv()
api_key = os.getenv('HUGGINGFACE_ACCESS_TOKEN')

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="conversational",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm = llm)


st.header("Research Tool")

paper_input = st.selectbox("Select research paper Name: ", ["Attention is All you Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT3: Language Models are Few-Shot Learners"])

style_input = st.selectbox("Select Explanation Style: ", ["Beginner-friendly", "Technical" , "Code-oriented"])

length_input = st.selectbox("Select Length: ", ["Short: (1-2) paragraph", "Medium: (3-5) paragraphs", "Long(detailed explanation)"])

template = load_prompt('template.json')

if st.button("Summarize"):
    chain = template | model 

    respond = chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input, 
    'length_input' : length_input
    })
    
    st.write(respond.content)





