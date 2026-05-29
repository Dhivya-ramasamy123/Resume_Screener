# 🎯 Resume Screener

A lightweight AI-powered resume screening tool built with **Streamlit** and **GROQ LLaMA3**.  
Paste a job description, upload a resume — get an instant **Fit / Not Fit** verdict with a reason.

---

## 📸 Preview

```
✅ Fit for the Role
The candidate has 4 years of Python experience and strong FastAPI skills
which directly match the role requirements. Their background in REST API
design and PostgreSQL aligns well with the tech stack listed in the JD.
```

```
❌ Not Fit for the Role
The role requires AWS and Kubernetes experience which are not mentioned
anywhere in the resume. The candidate's profile is backend-focused but
lacks the cloud infrastructure skills listed as mandatory.
```

---

## 📁 Project Structure

```
resume_screener/
│
├── app.py                  ← Entry point (Streamlit wiring)
│
├── core/
│   ├── llm.py              ← GROQ LLM client initialisation
│   └── screener.py         ← Prompt + LLM call + verdict parsing
│
├── utils/
│   └── extractor.py        ← PDF / DOCX → plain text extraction
│
├── ui/
│   └── components.py       ← All Streamlit render functions
│
├── requirements.txt
├── .env.template
└── README.md
```

---

## ⚙️ Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| UI        | Streamlit                           |
| LLM       | GROQ API — `llama3-8b-8192` (free)  |
| LLM SDK   | `langchain-groq`                    |
| PDF parse | `pypdf`                             |
| DOCX parse| `python-docx`                       |
| Config    | `python-dotenv`                     |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Resume_Screener.git
cd Resume_Screener
```

### 2. Create a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your GROQ API key

```bash
cp .env.template .env
```

### 5. Run the app

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## 🧠 How It Works

```
User Input
    │
    ├── Paste Job Description  (text area)
    └── Upload Resume          (PDF or DOCX)
            │
            ▼
    utils/extractor.py
    Extracts plain text from the uploaded file
            │
            ▼
    core/screener.py
    Builds a prompt → calls GROQ LLaMA3
            │
            ▼
    LLM Response parsed into:
    VERDICT: Fit / Not Fit
    REASON:  2–3 sentence explanation
            │
            ▼
    ui/components.py
    Renders the result card in Streamlit
```

---

## 📄 Supported File Types

| Format | Support |
|--------|---------|
| PDF    | ✅ Text-based PDFs |
| DOCX   | ✅ Microsoft Word  |
| DOC    | ✅ Legacy Word     |
| Image-based PDF | ❌ Not supported |


## 📦 requirements.txt

```
streamlit
langchain-groq
pypdf
python-docx
python-dotenv
```


