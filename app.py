import os
from dotenv import load_dotenv
load_dotenv()
from langchain_ollama import OllamaLLM
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#LangchainSmith Tracking
os.environ['LANGCHAIN_API_KEY']="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"
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

#Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question:{question}")
    ])

#Streamlit Framework
st.title("LangChain Demo With Gemma 2 Model")
input_text=st.text_input("What question do you have in mind?")

# Ollam Gemma Model
llm = OllamaLLM(model="gemma:latest") 
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

