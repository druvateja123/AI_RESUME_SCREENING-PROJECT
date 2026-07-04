import os
import fitz
import google.generativeai as genai
from dotenv import load_dotenv

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env file")
    exit()

genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Function to Extract PDF Text
# -----------------------------
def extract_text(pdf_path):
    text = ""

    try:
        if not os.path.exists(pdf_path):
            print(f"ERROR: File not found -> {pdf_path}")
            return ""

        doc = fitz.open(pdf_path)

        for page in doc:
            page_text = page.get_text()
            if page_text:
                text += page_text + "\n"

        doc.close()

    except Exception as e:
        print(f"Error reading {pdf_path}")
        print(e)

    return text.strip()


# -----------------------------
# Read Prompt Template
# -----------------------------
prompt_path = "prompts/prompt.txt"

if not os.path.exists(prompt_path):
    print("Prompt file not found!")
    exit()

with open(prompt_path, "r", encoding="utf-8") as file:
    prompt_template = file.read()


# -----------------------------
# Read Job Description
# -----------------------------
jd_path = "Job_Descriptions/JD_AI Engineer.pdf"

print("\nCurrent Working Directory:")
print(os.getcwd())

print("\nChecking Job Description File...")
print("Exists:", os.path.exists(jd_path))
print("Full Path:", os.path.abspath(jd_path))

job_description = extract_text(jd_path)

print("\nJob Description Length:", len(job_description))

if len(job_description) == 0:
    print("\nERROR: Job Description is empty.")
    exit()

print("\nJob Description Loaded Successfully!\n")


# -----------------------------
# Resume Folder
# -----------------------------
resume_folder = "Resumes"

if not os.path.exists(resume_folder):
    print("Resume folder not found!")
    exit()

resume_files = [f for f in os.listdir(resume_folder) if f.lower().endswith(".pdf")]

if len(resume_files) == 0:
    print("No PDF resumes found.")
    exit()


# -----------------------------
# Process Each Resume
# -----------------------------
for file in resume_files:

    print("\n" + "=" * 80)
    print(f"Analyzing Resume: {file}")
    print("=" * 80)

    resume_path = os.path.join(resume_folder, file)

    resume_text = extract_text(resume_path)

    if len(resume_text) == 0:
        print("Could not extract text from this resume.")
        continue

    prompt = prompt_template.format(
        job_description=job_description,
        resume=resume_text
    )

try:
    response = model.generate_content(prompt)
    print(response.text)

    import re

    match = re.search(r"match score[:\s]*(\d+)", response.text.lower())

    if match:
        score = int(match.group(1))

        if score >= 80:
            print("\n========== INTERVIEW SCHEDULE ==========")
            print("Status          : Shortlisted")
            print("Interview Date  : Tomorrow")
            print("Interview Time  : 10:00 AM")
            print("Interview Mode  : Google Meet")
            print("========================================")

        elif score >= 60:
            print("\nStatus : Manual Review")

        else:
            print("\nStatus : Rejected")

    else:
        print("\nMatch Score not found.")

except Exception as e:
    print("\nGemini API Error")
    print(e)


print("\n" + "=" * 80)
print("Resume Screening Completed Successfully!")
print("=" * 80)
