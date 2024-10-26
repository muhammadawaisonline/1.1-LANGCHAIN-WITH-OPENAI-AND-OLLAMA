import os 
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import ollama
import streamlit as st
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Lang Smith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"

prompt = ChatMessagePromptTemplate.format_messages(
    [
        ("system", "You are a helpful assitant. Please respond to the asked question"),
        ("user", "Question:{question}")
    ]
)

#Streamlit Framework
st.title("LANGCHAIN LLM MODEL with LlAMA3.2")
text_input=st.text_input("What question do you have in mind?")

##Ollama Llama 3.2 model
llm = ollama("llama3.2")
output_parser=StrOutputParser()
chain = prompt | llm | output_parser

if text_input:
    st.write(chain.invoke({"question": {text_input}}))
    