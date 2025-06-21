import streamlit as st

from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.runnables.history import RunnableWithMessageHistory
import os

from dotenv import load_dotenv

load_dotenv()
os.environ['HUGGINGFACE_API_KEY'] = os.getenv("HUGGINGFACE_API_KEY")

embeddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

st.title("Conversational RAG With PDF uploads and chat history")
st.write("Upload PDF's and chat with their content")

api_key=st.text_input("Upload Groq API Key",type="password")

if api_key:
    llm=ChatGroq(groq_api_key=api_key,model_name="Gemma2-9b-It")

    session_id=st.text_input("Session ID",value = "default_session")

    if "store" not in session_id:
        pass