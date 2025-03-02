# LegalShield — AI-Powered Legal Assistance Chatbot⚖️

LegalShield is an AI-driven legal assistant designed to simplify legal processes by providing instant legal support, document drafting, and document review. It enables users to generate legal documents, analyze contracts, and get legal information efficiently.  

---

## Key Features  

### **AI-Powered Legal Chatbot**  
- Get instant responses to legal queries using **Gemini API**.  
- User-friendly interface to ask questions about legal topics.  

### **Legal Document Drafting**  
- Generate various legal documents such as:  
  - Contracts  
  - Wills  
  - Non-Disclosure Agreements (NDAs)  
  - Custom legal documents  
- Interactive forms to collect necessary legal details.  

### **Document Review & Summarization**  
- Upload legal documents for **AI-based analysis**.  
- Get summaries and key insights from contracts and legal agreements.  

### **FAQ & Knowledge Base**  
- Provides AI-generated answers to common legal questions.  
- Helps users understand legal concepts easily.  

### **Legal Resources**  
- A repository of legal guidelines, rights, and references.  

---

## Tech Stack  

### **Frontend**  
- **Streamlit**: Interactive web UI.  

### **Backend**  
- **FastAPI**: Handles API requests and chatbot logic.  
- **Gemini API**: AI-powered legal chatbot responses.  

### **Libraries & Tools**  
- **PyMuPDF**: Legal document analysis.  
- **ReportLab**: PDF generation for legal documents.  

---

## How to Run the Project  

### **1. Clone the Repository**  
```sh
git clone https://github.com/sagar1024/Christ-CPCG-Hackathon.git
cd Christ-CPCG-Hackathon
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

3. Run the Backend (FastAPI)

```sh
cd backend
uvicorn main:app --reload
```

4. Run the Frontend (Streamlit)
```sh
cd frontend
streamlit run app.py
```
