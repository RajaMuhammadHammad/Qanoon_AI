# ⚖️ QanoonAI – Pakistani Legal Assistant

QanoonAI is an AI-powered legal assistant built to answer questions related to Pakistani laws. It leverages Google Gemini for generative responses, FAISS for semantic search in law documents, and a modern Flask-based web frontend.

---

## 🚀 Features

- 🧠 **Gemini-Powered Answers**: Uses Gemini 2.0 Flash to generate structured legal responses.
- 📚 **Semantic Search**: Searches relevant Pakistani law documents using FAISS vector search.
- 📄 **Legal Context Awareness**: Answers are backed by actual law sections with source references.
- 💬 **Chat UI**: Interactive and clean chat interface for user questions.
- ✅ **BERTScore Evaluation**: Evaluates answer quality against retrieved legal context.
- 🔐 **Secure API Handling**: Uses environment variables to keep your Gemini API key safe.

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (custom + Font Awesome), JavaScript
- **Backend**: Python Flask
- **LLM**: Google Gemini 2.0 Flash via API
- **Search**: FAISS (semantic vector search)
- **Deployment**: Render.com (free tier)

---

## 🧪 Getting Started (Local Setup)

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/QanoonAI-Legal-Assistant.git
cd QanoonAI-Legal-Assistant
