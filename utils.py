import fitz
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Connect to Groq with open source LLaMA model
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(pdf_file):
    """Reads a PDF file and returns all text as a string"""
    text = ""
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text += page.get_text()
    return text.strip()

def analyze_resume(resume_text, job_description):
    """Send both texts to LLaMA 3 via Groq and get analysis"""

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

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Free open source model
        messages=[
            {
                "role": "system",
                "content": "You are an expert HR recruiter. Always respond with valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1  # Low temperature = more consistent JSON output
    )

    # Clean and parse JSON response
    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    result = json.loads(raw)
    return result