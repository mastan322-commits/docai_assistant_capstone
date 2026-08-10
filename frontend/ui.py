import streamlit as st
import requests
import mimetypes

st.title("DocAI Assistant")

# Upload document
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "csv", "xlsx"])
if uploaded_file:
    # Ensure filename and MIME type are passed
    mime_type = mimetypes.guess_type(uploaded_file.name)[0] or "application/octet-stream"
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), mime_type)}
    response = requests.post("http://127.0.0.1:8080/upload-document/", files=files)
    st.write(response.json())

# Ask a question
question = st.text_input("Ask a question about your documents:")
if st.button("Submit"):
    response = requests.post("http://127.0.0.1:8080/ask-questions/", data={"question": question})
    st.write(response.json())

# Health check
if st.button("Check API Health"):
    response = requests.get("http://127.0.0.1:8080/health-check")
    st.write(response.json())
