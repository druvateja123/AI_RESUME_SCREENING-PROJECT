# AI Resume Screening System

# Project Overview
The AI Resume Screening System is a Python-based application that leverages Google's Gemini AI model to evaluate resumes against a given job description. The system extracts text from PDF files, analyzes the candidate's skills and qualifications, and generates a detailed evaluation report including a match score and hiring recommendation.

---
# Features
- Reads Job Description from a PDF file
- Reads multiple Resume PDF files
- Extracts text using Python
- Uses Google Gemini AI (Gemini 2.5 Flash) for resume analysis
- Generates:
  - Candidate Name
  - Match Score (%)
  - Matching Skills
  - Missing Skills
  - Hiring Recommendation
- Supports screening multiple resumes

---
# Technologies Used
- Python 3.13
- Google Gemini API
- PyPDF2
- python-dotenv
---
# Project Structure
AI-Resume-Screening/
│
├── Job_Descriptions/
│   └── JD_AI Engineer.pdf
│
├── Resumes/
│   ├── Resume-DavidJhon.pdf
│   ├── Resume-jhonson.pdf
│   ├── Resume-petter.pdf
│   └── Resume-TIMDAVID.pdf
│
├── prompts/
│   └── resume_prompt.txt
│
├── main.py
├── requirements.txt
├── README.md
├── .env.example

---
# Installation

# 1. Clone the repository
bash
git clone <repository-url>

or download the project ZIP.

---
# 2. Navigate to the project folder
bash
cd AI-Resume-Screening

---
# 3. Create a Virtual Environment
bash
python -m venv venv
---
# 4. Activate the Virtual Environment
Windows
bash
venv\Scripts\activate

---
# 5. Install Required Packages
bash
pip install -r requirements.txt
---
# 6. Configure Gemini API Key
Create a file named .env

Add:
text
GOOGLE_API_KEY=

Replace YOUR_API_KEY with your own Google Gemini API Key.
---
# Running the Project
Run the following command:
bash
python main.py

The application will process the Job Description and compare each resume with it.
---
# AI Prompt Used
The AI prompt instructs Gemini to:

- Compare Resume with Job Description
- Calculate Match Score
- Identify Matching Skills
- Identify Missing Skills
- Generate Hiring Recommendation

The prompt is stored in:
prompts/resume_prompt.txt

---
# Database Schema
No database is used in this project.
The application directly reads PDF files, processes them in memory, and sends the extracted text to the Gemini AI model for analysis.
---
# Sample Test Data

# Job Description
Job_Descriptions/JD_AI Engineer.pdf

# Sample Resumes
Resumes/Resume-DavidJhon.pdf
Resumes/Resume-jhonson.pdf
Resumes/Resume-petter.pdf
Resumes/Resume-TIMDAVID.pdf

These files are included for testing and demonstration purposes.

---
# Sample Output
The system generates:
Candidate Name: JOHNSON
Match Score: 95%

Matching Skills:
- Python
- SQL
- Machine Learning
- NLP
- FastAPI

Missing Skills:
- Power BI
- Microsoft Excel

Recommendation:
Highly suitable candidate for the AI Engineer role.
---
# Error Handling
The application handles:
- Missing PDF files
- Empty PDF files
- API connection issues
- Invalid API key
- Missing environment variables
---
# Future Improvements
- Web Interface using Streamlit or Flask
- Database Integration
- ATS Score Visualization
- Resume Ranking Dashboard
- Batch Resume Processing
- Export Results to Excel
- Support for DOCX resumes
---
# Author
Panta Druva Teja
M.Sc. Data Science and Analytics
AI Resume Screening System