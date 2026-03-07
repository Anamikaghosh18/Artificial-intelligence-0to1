from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace


llm = HuggingFacePipeline.from_model_id(
    model_id = '',
    task = 'conversation', 
    pipeline_kwargs=dict(
        temperature = 0.2 , 
        max_new_tokens = 100 
    )
)
model = ChatHuggingFace(llm= llm)

respond = model.invoke("what is the capital of india")
print(respond.content)