# 🤖 Smart HR Assistant: AI-Powered Knowledge System for Employee Insights

A Retrieval-Augmented Generation (RAG) based assistant built using FastAPI, LangChain, and ChromaDB that helps HR teams derive insights from structured employee data. Ask questions like "Which department has the most satisfied employees?" or "List employees likely to leave" and get precise answers.

---

## 🚀 Features

* 🔍 Ask natural language questions about employees
* 📊 View department-wise job satisfaction stats (via Chart.js)
* 🧠 Powered by **LLMs** using Groq + LLaMA-3 or Hugging Face models
* 🗂 Converts structured HR data (CSV) into text chunks for querying
* ⚡ Blazing fast retrieval using **Chroma Vector Database**
* 💻 Full-stack: FastAPI backend + HTML/CSS/JS frontend
* 🌐 Dockerized for ease of deployment
* 💎 Supports CSV upload for HR profiles

---

## 🛠️ Tech Stack

| Component       | Technology                           |
| --------------- | ------------------------------------ |
| Frontend        | HTML, CSS, JavaScript, Chart.js      |
| Backend         | Python, FastAPI                      |
| LLM Integration | Groq (LLaMA-3) / Hugging Face        |
| Embeddings      | Sentence Transformers (`all-MiniLM`) |
| Vector Store    | Chroma (aka ChromaDB)                |
| RAG Framework   | LangChain                            |
| Deployment      | Docker & Docker Compose              |

---

## 📁 Folder Structure

```
smart-hr-assistant/
│
├── backend/
│   ├── api/                # FastAPI route handlers
│   ├── core/               # RAG logic and vector pipeline
│   ├── employee_profiles.txt   # Embedded employee text data
│   ├── main.py             # FastAPI entry point
│   └── populate_vector_store.py # Script to populate ChromaDB
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 🔧 Step 1: Clone the repo

```bash
git clone https://github.com/Nithishkaranam2002/smart-hr-assistant.git
cd smart-hr-assistant
```

### 🔒 Step 2: Set environment variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key
EMBEDDING_MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2
```

If using Hugging Face:

```
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

---

## 🐳 Step 3: Run the app with Docker

```bash
docker compose up --build
```

This will:

* Install dependencies
* Launch FastAPI backend at `http://localhost:8000`

---

## 🧠 Step 4: Populate the Vector Store

```bash
python populate_vector_store.py
```

This script:

* Loads `employee_profiles.txt`
* Converts it to document chunks
* Embeds them using `all-MiniLM-L6-v2`
* Stores in Chroma vector store for fast querying

---

## 🌐 Step 5: Launch Frontend

In a separate terminal:

```bash
cd frontend
python3 -m http.server 5500
```

Then open: [http://localhost:5500](http://localhost:5500)

---

## 📄 Upload Employee CSV (Optional)

You can convert CSV to natural language using a script and append it to `employee_profiles.txt`.

Example format:

```
John is a Sales Executive with a Job Satisfaction score of 3.
Sarah works in HR and has a satisfaction score of 4.
```

---

## ✨ Example Questions

* “Which department has the happiest employees?”
* “List employees likely to leave.”
* “What is the average job satisfaction in Sales?”
* “How many employees are at risk of leaving?”

---

## 📊 Dashboard

Navigate to the **Dashboard** tab in the frontend to:

* View department-wise stats
* Compare job satisfaction or attrition visually using charts

---

## ✅ TODOs & Improvements

* Add auth layer (role-based)
* Enable document-based RAG (PDF/HR docs)
* Cloud deployment (Render, Railway, or AWS)
* Add chatbot-style frontend

---

## 🙌 Acknowledgements

* [LangChain](https://github.com/langchain-ai/langchain)
* [Chroma](https://www.trychroma.com/)
* [Groq](https://groq.com/)
* [Hugging Face](https://huggingface.co/)
* [Chart.js](https://www.chartjs.org/)

---

## 📄 License

MIT License © [Dimpu Nithish Karanam](https://github.com/Nithishkaranam2002)
