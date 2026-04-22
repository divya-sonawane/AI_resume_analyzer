import fitz  # PyMuPDF
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-lite")

def extract_text_from_pdf(pdf_file):
    """Reads a PDF file and returns all text as a string"""
    text = ""
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text += page.get_text()
    return text.strip()

def analyze_resume(resume_text, job_description):
    """Send both texts to Gemini and get analysis"""

    prompt = f"""
    You are an expert HR recruiter and resume analyst.

    RESUME TEXT:
    {resume_text}

    JOB DESCRIPTION:
    {job_description}

    Analyze the resume against the job description and return
    a JSON response with EXACTLY this format and nothing else:
    {{
      "match_score": 75,
      "matched_skills": ["Python", "Machine Learning", "SQL"],
      "missing_skills": ["Docker", "AWS", "React"],
      "strengths": ["Strong Python background", "Good project experience"],
      "improvements": ["Add Docker certification", "Mention cloud experience"],
      "summary": "Your resume is a good match but missing some key tech skills..."
    }}

    Return ONLY the JSON. No extra text. No markdown. No backticks.
    """

    response = model.generate_content(prompt)
    
    # Clean response and parse JSON
    raw = response.text.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    result = json.loads(raw)
    return result