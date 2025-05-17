from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFaceHub
import os

# Constants
CHROMA_DIR = "chroma_store"
EMPLOYEE_FILE = "employee_profiles.txt"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Load and split documents
def load_and_split_documents(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return text_splitter.split_documents(documents)

# Create embedding model
embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

# Create or load vector store
if not os.path.exists(CHROMA_DIR):
    os.makedirs(CHROMA_DIR)

# If file exists, load and index it
if os.path.exists(EMPLOYEE_FILE):
    documents = load_and_split_documents(EMPLOYEE_FILE)
    vectorstore = Chroma.from_documents(documents, embedding_model, persist_directory=CHROMA_DIR)
    vectorstore.persist()
else:
    raise FileNotFoundError(f"❌ {EMPLOYEE_FILE} not found!")

# Define RAG chain
llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature": 0.2, "max_length": 512})

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Answer the question based on the context below.

Context:
{context}

Question:
{question}
""",
)

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template}
)

# Function to ask a question
def ask_hr_question(query: str) -> str:
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(query)

    # 🔍 Debug: show what documents are retrieved
    print("\n🔍 Retrieved docs:")
    for doc in docs:
        print(doc.page_content)

    result = rag_chain.invoke({"query": query})
    return result["result"]

# (Optional) for FastAPI: employee stats endpoint
def get_employee_stats():
    with open(EMPLOYEE_FILE, "r") as f:
        lines = f.readlines()
    return {"total_employees": len(lines)}
