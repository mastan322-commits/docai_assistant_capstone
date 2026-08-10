import streamlit as st
import requests
import mimetypes

st.title("DocAI Assistant")

# Upload document
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "csv", "xlsx"])
if uploaded_file:
    mime_type = mimetypes.guess_type(uploaded_file.name)[0] or "application/octet-stream"
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), mime_type)}
    response = requests.post("http://127.0.0.1:8080/upload-document/", files=files)

    st.subheader("Upload Result")
    try:
        st.json(response.json())
    except Exception:
        st.error("Backend did not return JSON.")
        st.text(response.text)


# Ask a question
st.subheader("Ask a Question")
question = st.text_input("Enter your question:")
if st.button("Submit"):
    response = requests.post("http://127.0.0.1:8080/ask-questions/", data={"question": question})
    result = response.json()

    st.write("### Question")
    st.write(result.get("question", ""))

    st.write("### Top Retrieved Chunks")
    for i, chunk in enumerate(result.get("top_chunks", []), start=1):
        st.write(f"**Chunk {i}:** {chunk}")

    # If backend later adds LLM answer
    if "answer" in result:
        st.write("### Answer")
        st.write(result["answer"])
