import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

# Define the LLM model
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5)  # Use the appropriate model

# Define the prompt template for generating code
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="Generate a Python code snippet for the following request:\n{user_input}"
)

# Create the LLM chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit app
st.title("Code Generating Chatbot")
st.write("Ask me to generate code snippets in Python!")

user_input = st.text_input("Enter your request:")

if st.button("Generate Code"):
    if user_input:
        with st.spinner("Generating code..."):
            response = chain.run(user_input)
            st.code(response, language="python")
    else:
        st.error("Please enter a request.")
