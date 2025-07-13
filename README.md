# 🧠 Smart Assistant for Research Summarization

A **GenAI-powered local assistant** that intelligently reads your documents (PDF or TXT), summarizes them, answers deep and context-rich questions, challenges your understanding with logic-based questions, and justifies all responses with supporting evidence — all inside a sleek, interactive UI.

---

## 📌 Problem Statement

Reading through lengthy research papers, legal documents, or technical manuals can be overwhelming. Traditional tools often lack contextual understanding, inference, and reasoning capabilities.

**This AI assistant solves that by:**

* 🧾 Providing intelligent summaries using BART
* ❓ Answering user questions grounded in the uploaded document
* 🧠 Generating logic-based challenge questions
* 📎 Justifying every answer with document-based evidence

---

## ✨ Key Features

| Feature                    | Description                                    |
| -------------------------- | ---------------------------------------------- |
| 📤 **Document Upload**     | Upload `.pdf` or `.txt` files                  |
| 🧠 **Auto Summary**        | Generates a ≤150-word summary using BART       |
| 💬 **Ask Anything**        | Ask any question and get a contextual answer   |
| 📎 **Justified Answers**   | Includes the exact snippet used as evidence    |
| 🎯 **Challenge Mode**      | Logic-based system-generated Q\&A              |
| 🔦 **Answer Highlighting** | Highlights relevant document sections          |
| 🧠 **Chat Memory**         | Displays recent interactions for continuity    |
| 🎨 **Minimal UI**          | Clean, accessible layout with intuitive design |

---

## 🧰 Technologies Used

* **Streamlit** — Frontend interface
* **Hugging Face Transformers** — BART (summarization), DistilBERT (QA)
* **PyPDF2** — PDF parsing and text extraction
* **dotenv** — For handling API keys securely
* **Python** — Backend logic and pipeline orchestration

---

## 📂 Folder Structure

```bash
smart-assistant/
│
├── app.py                  # Main Streamlit application
├── documentloader.py       # Loads and extracts text from PDF/TXT files
├── summarizer.py           # Summarizes documents using BART
├── qaengine.py             # QnA model logic using HuggingFace pipeline
├── challengemode.py        # Challenge-mode logic and evaluation
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (e.g. API keys) [Optional]
├── assets/                 # (Optional) UI screenshots or icons
│   ├── upload.png
│   ├── ask.png
│   └── challenge.png
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-assistant.git
cd smart-assistant
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

<sub>If any dependency fails, install separately:</sub>

```bash
pip install streamlit PyPDF2 transformers python-dotenv
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

### 5. Access the App

Open your browser and visit:

```
http://localhost:8501
```

---

## 🔧 Future Enhancements (Ideas)

* 🧠 Advanced memory (RAG or LangChain-style context chaining)
* 🌐 Export answers/summaries to PDF
* 💡 Add multi-document summarization
* 🎙️ Voice-based Q\&A interface
* 🪄 Use larger language models via OpenAI/Gemini APIs

---

## 👩‍💻 Built with ❤️ by [Ananyaa Sharrma](mailto:ananyaa00051@gmail.com)

---
