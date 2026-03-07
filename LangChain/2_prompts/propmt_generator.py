from langchain_core.prompts import PromptTemplate


template = PromptTemplate(
    template = '''
You are an expert research assistant Summarizer. Your task is to provide concise, accurate, and structured information based on the users query 
Summarize the research paper : {paper_input}
Explanation Style : {style_input}
Explanation Length : {length_input}

''', 

input_variables = ['paper_input', 'style_input', 'length_input']
)

template.save('template.json')
