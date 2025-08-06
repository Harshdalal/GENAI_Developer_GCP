
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Setup API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
assert GOOGLE_API_KEY, "GOOGLE_API_KEY not found in .env"

# Load vector store
@st.cache_resource
def load_vectorstore():
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001", google_api_key=GOOGLE_API_KEY
    )
    return FAISS.load_local("vectorstore", embedding_model, allow_dangerous_deserialization=True)

# Setup Gemini LLM
def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3
    )

# Create a retrieval-based QA chain
def create_qa_chain(llm, vectorstore):
    prompt_template = """
    You are a helpful banking assistant. Answer the user query using only the given context.
    If the answer is not in the context, say "Sorry, the policy information is not available."

    Context:
    {context}

    Question:
    {question}
    """

    prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
    return qa_chain

# Streamlit UI
def main():
    st.set_page_config(page_title="🧠 Internal Banking Policy Assistant", layout="wide")
    st.title("🏦 Internal Banking Policy Assistant")
    st.write("Ask about KYC rules, loan eligibility, compliance, etc.")

    # Load models
    vectorstore = load_vectorstore()
    llm = get_llm()
    qa_chain = create_qa_chain(llm, vectorstore)

    # User input
    query = st.text_input("Enter your query:", placeholder="E.g. What are the KYC rules for opening a savings account?")

    if st.button("Ask") and query:
        with st.spinner("🔍 Searching policy documents..."):
            result = qa_chain(query)

        st.subheader("📄 Answer:")
        st.write(result['result'])

        with st.expander("📚 Source Documents"):
            for doc in result["source_documents"]:
                st.markdown(f"**File**: {doc.metadata.get('source', 'N/A')}")
                st.text(doc.page_content[:500])  # Show first 500 chars

if __name__ == "__main__":
    main()
