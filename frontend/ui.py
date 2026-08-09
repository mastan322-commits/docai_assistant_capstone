import streamlit as st
import requests

st.title("DocAI Assistant")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "csv", "xlsx"])
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/upload-document/", files=files)
    st.write(response.json())

question = st.text_input("Ask a question about your documents:")
if st.button("Submit"):
    response = requests.post("http://127.0.0.1:8000/ask-questions/", data={"question": question})
    st.write(response.json())

if st.button("Check API Health"):
    response = requests.get("http://127.0.0.1:8000/health-check")
    st.write(response.json())
