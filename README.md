# CLATLegalExamQueryChatbot
Sure! Here's a polished and professional `README.md` tailored for your GitHub repo. It integrates your exact requirements and frames them in a clean, developer-friendly format:

---

# ⚖️ CLAT Legal Exam Query Chatbot

A lightweight and modular chatbot built to assist users with **CLAT (Common Law Admission Test)** preparation queries. This prototype is designed using a rule-based/NLP approach, deployable via **Streamlit** for instant access.

---

## 📌 Problem Statement

**Goal:** Build a simple chatbot prototype that can handle CLAT-related queries through either rule-based logic or natural language processing (NLP).

The chatbot should:
- Accept a user query via a web interface.
- Search a predefined knowledge base (or open-source data).
- Respond with the most relevant answer using basic NLP methods (e.g., spaCy similarity, keyword matching).

---

## 🔍 Sample Use Cases

These are example queries the chatbot can currently understand and respond to:

- **“What is the syllabus for CLAT 2025?”**
- **“How many questions are there in the English section?”**
- **“Give me last year’s cut-off for NLSIU Bangalore.”**

---

## 📚 Current Knowledge Base

> **Note:** This is an MVP using a small, static knowledge base for demonstration. You can expand it as needed.

| Query Intent | Sample Answer |
|--------------|---------------|
| **Syllabus** | CLAT 2025 syllabus includes English, Current Affairs, Legal Reasoning, Logical Reasoning, and Quantitative Techniques. |
| **English Section Questions** | There are around 28–32 questions in the English section. |
| **NLSIU Cutoff** | The cut-off for NLSIU Bangalore in 2024 was around 85 for the general category. |
| **Exam Duration** | The CLAT exam duration is 2 hours. |
| **Application Deadline** | The last date to apply for CLAT 2025 is expected to be in November 2024. |

---

## 🧠 Architecture Overview

This application follows the **SOLID principles** and is broken into clean, maintainable components:

```
clat_chatbot/
├── dashboard.py         # Streamlit frontend UI
├── backend.py           # NLP logic using spaCy
├── knowledge_base.py    # Static knowledge base dictionary
├── requirements.txt     # For dependency management
└── README.md            # Project documentation
```

### 🔧 Technologies Used

- **Python 3**
- **spaCy** (`en_core_web_sm` for lightweight NLP)
- **Streamlit** (for the interactive web app)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/clat-chatbot.git
cd clat-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run dashboard.py
```

---

## 🌍 Deployment (Streamlit Cloud)

This project is optimized for **Streamlit Cloud free tier**:
- Small model (`en_core_web_sm`)
- Minimal dependencies
- Easy to deploy directly from GitHub

> Just upload the repo and deploy on [https://share.streamlit.io](https://share.streamlit.io)

---

## 🎯 Future Scope & Scaling Suggestions

To elevate this chatbot beyond rule-based logic:

### 🔁 GPT-based Upgrade (Bonus)
- Fine-tune a **GPT-style model** on NLTI’s curated CLAT training material.
- Format training data in QA pairs like:
  ```
  User: What is the syllabus for CLAT?
  Bot: The syllabus includes English, Legal Reasoning...
  ```
- Use RAG (retrieval-augmented generation) with tools like **Haystack** or **LlamaIndex** for dynamic document-based answering.

---

## 🧑‍💼 Author

**Vikram Singh**  
For academic collaborations, contributions, or product integration: <a href="https://www.linkedin.com/in/vikramkumarsingh0/">[LinkedIn]</a>#https://www.linkedin.com/in/vikramkumarsingh0/)

---
