import streamlit as st
from langchain_ollama.llms import OllamaLLM
# assigning ollama llm
llm=OllamaLLM(model="codellama")
st.title("Coding Chatbot")
st.header("enter any question related to coding")
question=st.text_input(label="")
if question:
    response=llm.invoke(question)
    st.success(response)
