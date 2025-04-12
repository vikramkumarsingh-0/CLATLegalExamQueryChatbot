Absolutely! Here's the cleaned-up, **professional version of the README** with all icons and emojis removed, keeping the tone clear and polished:

---

# CLAT Legal Exam Query Chatbot

A modular chatbot designed to assist students preparing for the Common Law Admission Test (CLAT). This lightweight prototype leverages semantic similarity models for accurate responses and is deployed using a simple Streamlit interface.

---

## Objective

This project demonstrates how natural language understanding can be applied to build a domain-specific chatbot. It uses sentence-level embeddings to retrieve the most relevant answers from a predefined knowledge base.

---

## Features

- Natural language query processing
- Semantic similarity matching using Sentence Transformers
- User-friendly web interface via Streamlit
- Easily extensible static knowledge base
- Compatible with Python 3.12 and deployable on Streamlit Cloud

---

## Example Queries

The chatbot can currently respond to questions like:

- What is the syllabus for CLAT 2025?
- How many questions are there in the English section?
- What was the cut-off for NLSIU Bangalore in 2024?
- What is the exam duration for CLAT?
- When is the last date to apply for CLAT 2025?

---

## Sample Knowledge Base

| Query Category           | Sample Response                                                                 |
|--------------------------|----------------------------------------------------------------------------------|
| CLAT Syllabus            | CLAT 2025 syllabus includes English, Current Affairs, Legal Reasoning, Logical Reasoning, and Quantitative Techniques. |
| English Section          | There are approximately 28–32 questions in the English section.                 |
| NLSIU Cutoff (2024)      | The general category cut-off for NLSIU Bangalore in 2024 was around 85.         |
| Exam Duration            | The total exam duration is 2 hours.                                             |
| Application Deadline     | The last date to apply for CLAT 2025 is expected to be in November 2024.       |

---

## Project Structure

```
clat_chatbot/
├── backend.py           # Core NLP logic using Sentence Transformers
├── dashboard.py         # Streamlit interface for interaction
├── knowledge_base.py    # Static question-answer dataset
├── requirements.txt     # Python 3.12-compatible dependencies
└── README.md            # Project documentation
```

---

## Technologies Used

- Python 3.12
- Sentence Transformers (all-MiniLM-L6-v2)
- PyTorch
- Streamlit

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/clat-chatbot.git
cd clat-chatbot
```

### 2. Set Up Virtual Environment

```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run dashboard.py
```

---

## Deployment

This application is optimized for hosting on Streamlit Cloud. You can deploy it by linking the repository directly through [https://share.streamlit.io](https://share.streamlit.io).

---

## Future Development

- Replace the static knowledge base with a document retrieval system.
- Integrate a fine-tuned GPT model using QA pairs from NLTI’s legal preparation data.
- Use RAG frameworks such as Haystack or LlamaIndex for dynamic document-based answering.
- Add feedback loops and query logging for performance evaluation.

---

## Author

**Vikram Singh**  
For inquiries, contributions, or collaborations: [LinkedIn Profile](https://www.linkedin.com/in/vikramkumarsingh0/)

---
