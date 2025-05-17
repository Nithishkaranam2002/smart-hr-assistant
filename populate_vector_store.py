import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

CHROMA_DIRECTORY = "chroma_store"
EMPLOYEE_FILE = "employee_profiles.txt"



# ✅ Step 1: Check file exists
if not os.path.exists(EMPLOYEE_FILE):
    raise FileNotFoundError(f"❌ {EMPLOYEE_FILE} not found!")

# ✅ Step 2: Read each line and convert to document
with open(EMPLOYEE_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

documents = [Document(page_content=line) for line in lines]

# ✅ Step 3: Create embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ✅ Step 4: Populate Chroma DB
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory=CHROMA_DIRECTORY
)

vectorstore.persist()
print("✅ Vector store populated successfully!")
