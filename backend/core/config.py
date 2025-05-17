# backend/core/config.py
import os
from dotenv import load_dotenv

# Get absolute path to the root directory where .env is located
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOTENV_PATH = os.path.join(ROOT_DIR, ".env")

# Load .env manually
load_dotenv(dotenv_path=DOTENV_PATH)

# Pull the environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Optional safety check
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is missing from your .env file!")

# Other config values
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
CHROMA_DIRECTORY = "chroma_store"
LLAMA_MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"
