# 🧠 AI Resume Screening System

An AI-powered resume screening system built using LangChain and Groq, with full pipeline tracing using LangSmith.

---

## 🚀 Features

- Resume + Job Description Input
- Skill Extraction
- Matching Analysis
- Candidate Scoring (0–100)
- Explanation Generation
- LangSmith Tracing (Debugging)
- Groq API Integration
- PDF Resume Support

---

## 🛠 Tech Stack

- Python
- LangChain
- Groq (LLM)
- LangSmith (Tracing)
- PyPDF2

---
## 📂 Project Structure

```
ai-resume-screening/
│
├── prompts/
│   ├── extraction_prompt.py
│   ├── matching_prompt.py
│   ├── scoring_prompt.py
│   ├── explanation_prompt.py
│
├── chains/
│   ├── extraction_chain.py
│   ├── matching_chain.py
│   ├── scoring_chain.py
│   ├── explanation_chain.py
│
├── data/
│   ├── resumes/
│   ├── job_description.txt
│
├── main.py
├── requirements.txt
└── README.md
```
---

## ⚙️ Setup Instructions

### 1. Clone Repository
git clone <your-repo-link>
cd AI-Resume_Screening

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Setup Environment Variables

Create `.env` file:
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=resume-screening

---

## ▶️ Run the Project
python main.py

---

## 📊 Pipeline Flow
Resume → Skill Extraction → Matching → Scoring → Explanation → Tracing


---

## 🔍 LangSmith Tracing

- Tracks each pipeline step
- Helps debug incorrect outputs
- Shows LLM inputs and outputs

---

## 📸 Output

- Terminal Output (formatted)
- Saved Output File
- LangSmith Dashboard
- Groq API Logs

---

## 🎯 Evaluation Criteria Covered

✔ Pipeline Design  
✔ LangChain Implementation  
✔ Scoring Logic  
✔ Explainability  
✔ LangSmith Tracing  
✔ Code Structure  

---

## 💡 Future Improvements

- Streamlit UI
- JSON structured outputs
- Better scoring algorithm
- Resume ranking system