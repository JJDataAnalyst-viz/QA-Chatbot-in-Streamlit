# 📚 Conversational RAG with PDF Uploads and Chat History

An interactive Streamlit application that lets you **upload PDFs and chat with their content** using a modern **RAG (Retrieval-Augmented Generation)** architecture. Powered by **Groq’s blazing-fast LLMs**, **HuggingFace embeddings**, and **LangChain**, this tool brings intelligent, document-aware conversations to life.

---

## 🚀 Features

- 📄 **Upload PDFs** – Drop in any PDF and chat with its contents.
- 🧠 **Conversational Memory** – Maintains chat history using LangChain’s memory module.
- ⚡ **Groq-Powered LLM** – Leverages `Gemma 2 9B-It` via Groq for ultra-fast and fluent answers.
- 🔍 **Smart Retrieval** – Semantic chunk retrieval using `all-MiniLM-L6-v2` embeddings.
- 🛠️ **LangChain Integration** – Modular and flexible chain architecture using LangChain.
- 💡 **Perfect for Research, Study, and Knowledge Mining**.

---

## 🧑‍💻 Tech Stack

| Component        | Description                                  |
|------------------|----------------------------------------------|
| Frontend         | [Streamlit](https://streamlit.io)            |
| LLM              | [Groq](https://groq.com) - `Gemma 2 9B-It`   |
| Embeddings       | HuggingFace `all-MiniLM-L6-v2`               |
| Vector Store     | [Chroma](https://www.trychroma.com/)         |
| PDF Loader       | LangChain’s `PyPDFLoader`                    |
| Chain Framework  | [LangChain](https://www.langchain.com)       |
| Environment Vars | `python-dotenv`                              |

---

## 🧠 How It Works

1. **PDF Upload** → You select a `.pdf` file.
2. **Text Extraction** → PDF content is extracted and split into chunks.
3. **Embeddings** → Chunks are embedded with `all-MiniLM-L6-v2`.
4. **Vector Store** → Chunks are stored in Chroma for fast semantic search.
5. **LLM Q&A** → Groq's Gemma2-9B-It answers your question using relevant chunks.
6. **Memory** → Past messages are remembered for contextual understanding.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/conversational-pdf-rag.git
cd conversational-pdf-rag
```
2. Install dependencies
```bash
Copy code
pip install -r requirements.txt
```
3. Create a .env file

```bash
HUGGINGFACE_API_KEY=your_huggingface_api_key
```
The Groq API key is entered inside the app interface (for security).

4. Run the Streamlit app
```bash
Copy code
streamlit run app.py
```


# 📸 Screenshots
---
---

# 🗂 Example Project Structure
```bash
Copy code
conversational-pdf-rag/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── .streamlit/
```
# 📄 License
MIT License. Feel free to fork, use, and modify.

# 🙋‍♂️ Contributions
Pull requests and ideas welcome! If you find this useful, ⭐️ star the repo and share it.

