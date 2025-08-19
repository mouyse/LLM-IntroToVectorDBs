# Intro to VectorDBs with LangChain & Pinecone

This project demonstrates how to ingest text data, split it into chunks, embed it using OpenAI, and store/retrieve it from Pinecone using **LangChain**.

## 📂 Project Structure

```
IntroToVectorDBs/
│── ingestion.py       # Script to load, split, embed, and ingest documents
│── wikipedia.txt      # Sample document (Mahabharata article)
│── Pipfile            # Pipenv dependencies
│── Pipfile.lock       # Locked dependencies
│── .env.example       # Example environment variables (do not commit real .env)
│── README.md          # Documentation
```

## ⚡ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/mouyse/LLM-IntroToVectorDBs.git
cd LLM-IntroToVectorDBs
```

### 2. Install Dependencies
This project uses **Pipenv**:
```bash
pip install pipenv
pipenv install
```

Or, if you prefer `pip`:
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory based on `.env.example`:
```ini
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
INDEX_NAME=your_pinecone_index
OPENAI_API_TYPE=openai
```

⚠️ Never commit your real `.env` to GitHub.

### 4. Run Ingestion
```bash
pipenv run python ingestion.py
```

This will:
1. Load `wikipedia.txt`
2. Split it into 1000-character overlapping chunks
3. Embed chunks using OpenAI embeddings
4. Store embeddings in Pinecone under your `INDEX_NAME`

---

## 📚 Tech Stack
- [LangChain](https://www.langchain.com/) – LLM orchestration  
- [OpenAI](https://platform.openai.com/) – Text embeddings  
- [Pinecone](https://www.pinecone.io/) – Vector database  
- [Pipenv](https://pipenv.pypa.io/) – Dependency management  

---

## 🤝 Contributing
Pull requests are welcome! Please fork the repo and open a PR.

---

## 📜 License
MIT License © 2025 [Jay Shah]
