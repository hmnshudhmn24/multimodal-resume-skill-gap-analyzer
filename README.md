# 🧠 Multimodal Resume Skill Gap Analyzer

A smart, end-to-end **AI-powered system** that analyzes **PDF resumes**, **GitHub text**, and **LinkedIn content** to identify **missing skills** and generate a **personalized learning roadmap** with prioritized skills and learning resources.

Designed for **career growth, upskilling, and recruiter-facing portfolios**.

---

## 🚀 Key Features

- 📄 Resume parsing (PDF/DOCX support)
- 🧑‍💻 GitHub profile & repository text analysis
- 🔗 LinkedIn text ingestion
- 🧹 Text cleaning & preprocessing
- 🧠 Skill extraction using taxonomy + NLP
- 📉 Skill gap detection
- 📊 Skill prioritization & ranking
- 🗺️ Personalized learning roadmap generation
- 📝 Report generation (Markdown)
- 🔒 Fully local & privacy-friendly

---

## 🧠 System Pipeline

```
Resume / GitHub / LinkedIn
        ↓
Text Ingestion
        ↓
Preprocessing & Cleaning
        ↓
Skill Extraction
        ↓
Skill Gap Analysis
        ↓
Skill Ranking
        ↓
Personalized Learning Roadmap
```

---

## 📁 Project Structure

```
multimodal-resume-skill-gap-analyzer/
├── app/
├── config/
├── data/
├── scripts/
├── tests/
├── docs/
└── README.md
```

---

## 🛠️ Tech Stack

- **Language:** Python  
- **NLP:** Rule-based + keyword extraction  
- **ML:** Embeddings, similarity scoring  
- **Resume Parsing:** PyPDF2  
- **Validation:** Pydantic  

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python scripts/run_demo.py
```

---

## 📊 Output

- 📄 Skill gap report (`data/reports/roadmap.md`)
- 📌 Prioritized list of missing skills
- 🗺️ Clear learning roadmap for career growth

---

## 🎯 Use Cases

- Students planning learning paths
- Job seekers preparing for roles
- Career counselors & mentors
- EdTech platforms

---

## 🔮 Future Enhancements

- Hugging Face embeddings
- LLM-based roadmap generation
- Gradio / FastAPI UI
- PDF & HTML reports

---

## 📜 License

Apache License 2.0
