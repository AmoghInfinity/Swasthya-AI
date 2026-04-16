# 🩺 SwasthyaAI  
### Agentic RAG-Based Health & Diet Advisory System

SwasthyaAI is an **Agentic AI system** that provides intelligent health and diet recommendations using a combination of **Retrieval-Augmented Generation (RAG)** and **multi-step agent reasoning**.

It delivers **context-aware, reliable, and structured responses** for common health conditions and dietary needs.

---

## 🚀 Features

### 🧠 Agentic AI System
- Multi-step decision making using LangGraph  
- Router-based execution (retrieve / tool / skip)  
- Modular node-based architecture  

### 📚 Retrieval-Augmented Generation (RAG)
- Domain-specific knowledge base  
- ChromaDB vector storage  
- Context-grounded answers (reduces hallucination)  

### 🥗 Health & Diet Guidance
- Diabetes-friendly diet recommendations  
- Fatty liver management  
- High protein diets (veg & non-veg)  
- Indian diet preferences  

### 🛠️ Tool Integration
- BMI Calculator  
- Extendable tool system  

### 💬 Modern UI
- Built with Streamlit  
- Chat-style interface  
- Red & white healthcare theme  

---

## 🏗️ Architecture

User Input  
↓  
Memory Node  
↓  
Router Node (decides path)  
↓  
[Retrieval Node (RAG)] OR [Tool Node] OR [Skip Node]  
↓  
Answer Node (LLM - Gemini)  
↓  
Final Response  

---

## ⚙️ Tech Stack

- **LLM**: Google Gemini (`gemini-flash-latest`)  
- **Agent Framework**: LangGraph  
- **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)  
- **Vector Database**: ChromaDB  
- **Backend**: Python  
- **Frontend**: Streamlit  

---

## 📁 Project Structure

SwasthyaAI/  
├── app/  
│   ├── graph.py  
│   ├── nodes.py  
│   ├── rag.py  
│   ├── tools.py  
│   └── __init__.py  
│  
├── data/  
│   └── documents.py  
│  
├── ui/  
│   └── streamlit_app.py  
│  
├── tests/  
│   ├── test_rag.py  
│   ├── test_tools.py  
│   ├── test_graph.py  
│  
├── requirements.txt  
├── README.md  
└── .gitignore  

---

## 🧪 Testing

The project includes tests for:

- RAG retrieval validation  
- Tool functionality  
- End-to-end agent pipeline  

Run tests:

python tests/test_rag.py  
python tests/test_tools.py  
python tests/test_graph.py  

---

## ▶️ How to Run

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/SwasthyaAI.git  
cd SwasthyaAI  

---

### 2. Create Virtual Environment

python -m venv venv  
venv\Scripts\activate  

---

### 3. Install Dependencies

pip install -r requirements.txt  

---

### 4. Add Environment Variables

Create a `.env` file:

GEMINI_API_KEY=your_api_key_here  

---

### 5. Run the Application

streamlit run ui/streamlit_app.py  

---

## 🧠 Key Highlights

- Uses **agentic architecture instead of a single LLM call**  
- Implements **RAG for factual accuracy**  
- Reduces hallucination via **context-constrained prompting**  
- Modular and extensible system design  

---

## ⚠️ Disclaimer

This application provides general health and diet suggestions and is **not a substitute for professional medical advice**.

---

## 👨‍💻 Author

Amogh Gupta  

---

## ⭐ Acknowledgements

- Google Gemini API  
- HuggingFace  
- ChromaDB  
- Streamlit  
