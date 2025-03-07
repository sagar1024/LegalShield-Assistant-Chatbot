## LegalShield — AI-Powered Legal Assistance Chatbot⚖️

LegalShield is an AI-driven legal assistant designed to simplify legal processes by providing instant legal support, document drafting, and document review. It enables users to generate legal documents, analyze contracts, and get legal information efficiently.  

---

## Key Features  

#### **1. AI-Powered Legal Chatbot**  
- Get instant responses to legal queries using **Gemini API**.  
- User-friendly interface to ask questions about legal topics.  

#### **2. Legal Document Drafting**  
- Generate various legal documents such as:  
  - Contracts  
  - Wills  
  - Non-Disclosure Agreements (NDAs)  
  - Custom legal documents  
- Interactive forms to collect necessary legal details.  

#### **3. Document Review & Summarization**  
- Upload legal documents for **AI-based analysis**.  
- Get summaries and key insights from contracts and legal agreements.  

#### **4. FAQ & Knowledge Base**  
- Provides AI-generated answers to common legal questions.  
- Helps users understand legal concepts easily.  

#### **5. Legal Resources**  
- A repository of legal guidelines, rights, and references.  

---

## Tech Stack  

#### **1. Frontend**  
- **Streamlit**: Interactive web UI.  

#### **2. Backend**  
- **FastAPI**: Handles API requests and chatbot logic.  
- **Gemini API**: AI-powered legal chatbot responses.  

#### **3. Libraries & Tools**  
- **PyMuPDF**: Legal document analysis.  
- **ReportLab**: PDF generation for legal documents.  

---

## How to Run the Project  

#### **1. Clone the Repository**  
```sh
git init
git clone https://github.com/sagar1024/Christ-CPCG-Hackathon.git
cd Christ-CPCG-Hackathon
```

#### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

#### 3. Create an .env file in the backend

Go to Google AI studio and create GeminiAPI Key and paste it in .env file. Create a varialble GEMINI_API_KEY and assign it your api key.

#### 4. Run the Backend (FastAPI)

```sh
cd backend
uvicorn app.main:app --reload
```

#### 5. Run the Frontend (Streamlit)
```sh
cd frontend
streamlit run app.py
```

## How the Application Works
1. User selects a feature (Chatbot, Document Drafting, Document Review, FAQs).
2. Chatbot provides instant responses to legal queries.
3. Legal Document Drafting allows users to enter details and generate PDFs.
4. Document Review analyzes uploaded legal documents.
5. Legal Resources provides useful legal references.

The entire system runs as an API-based application, ensuring speed, security, and efficiency.

## Contributors

##### Sagar Gurung

##### CHRIST University, Bangalore
