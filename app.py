import streamlit as st
from transformers import pipeline

# ✅ MUST be the first Streamlit command
st.set_page_config(page_title="Fast Question Answering System", layout="centered")

# Load the QA pipeline once with a lightweight model
@st.cache_resource
def load_model():
    return pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

qa_pipeline = load_model()

# UI layout
st.title("💬 Fast Question Answering System")
st.markdown("Provide a **context** and ask a **question**. The system will answer using DistilBERT.")

# Input fields
context = st.text_area("📄 Enter the context (passage):", height=250, placeholder="Paste your document or passage here...")
question = st.text_input("❓ Enter your question:", placeholder="What is the document about?")

# Process and display answer
if st.button("Get Answer"):
    if context.strip() == "" or question.strip() == "":
        st.warning("⚠️ Please enter both context and question.")
    else:
        with st.spinner("Thinking..."):
            result = qa_pipeline(question=question, context=context)
            st.success(f"✅ **Answer:** {result['answer']}")
