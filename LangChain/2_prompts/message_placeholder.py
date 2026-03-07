'''
    whenever we need to recall the previous message context we use message placeholder 
    to get the previous context and then next conversation will start from there only 
'''

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.messages import SystemMessage, HumanMessage


chat_template = ChatPromptTemplate([
    ("system" , "You are a helpful support agent"), 
    MessagesPlaceholder(variable_name='chat_history'),
    ("human" , "{query}"),
])

# load chat history 
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt 

chat_template.invoke({'chat_history': chat_history, "query":"where is the my refund"})