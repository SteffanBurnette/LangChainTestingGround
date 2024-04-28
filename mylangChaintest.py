#pip install langchain --user
#Make sure the Ollama server is running before executing the code
from langchain_community.llms import Ollama

#Here we are definig the model that is being used
llm = Ollama(model="llama3")
#Here we are asking the Ollama llama3 model a prompt and outputting the response
print(llm.invoke("how can langsmith help with testing?"))


#We can also guide its response with a prompt template. 
#Prompt templates convert raw user input to better input to the LLM.
from langchain_core.prompts import ChatPromptTemplate #importing to make the template
#Defining the prompt which will assign the llm a role and take in the value that the user inputs
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])

#Now we can combine these to inorder to create a chain
chain = prompt | llm 


#We can now invoke it and ask the same question. It still won't know the answer,
#but it should respond in a more proper tone for a technical writer!
chain.invoke({"input": "how can langsmith help with testing?"})