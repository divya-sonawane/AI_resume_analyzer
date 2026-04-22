import streamlit as st
from utils import extract_text_from_pdf, analyze_resume

# Page title and layout
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠")
st.title("🧠 AI Resume Analyzer & Job Matcher")
st.write("Upload your resume and paste a job description to get an AI match score!")

# Left side: PDF upload
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload Your Resume")
    resume_file = st.file_uploader("Choose a PDF file", type=["pdf"])

with col2:
    st.subheader("💼 Paste Job Description")
    job_desc = st.text_area("Paste the full job description here", height=200)

# Analyze button
if st.button("🔍 Analyze Resume", type="primary"):
    if not resume_file or not job_desc:
        st.warning("Please upload a resume AND paste a job description!")
    else:
        with st.spinner("AI is analyzing your resume... ⏳"):
            # Extract text from PDF
            resume_text = extract_text_from_pdf(resume_file)
            
            # Send to AI for analysis
            result = analyze_resume(resume_text, job_desc)
        
        # ── Display Results ──
        st.success("✅ Analysis Complete!")
        
        # Big match score
        score = result["match_score"]
        color = "green" if score >= 70 else ("orange" if score >= 40 else "red")
        st.markdown(f"### Match Score: :{color}[{score}%]")
        st.progress(score / 100)
        
        # Two columns for skills
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("✅ Matched Skills")
            for skill in result["matched_skills"]:
                st.success(skill)
        with c2:
            st.subheader("❌ Missing Skills")
            for skill in result["missing_skills"]:
                st.error(skill)
        
        # Improvements
        st.subheader("💡 How to Improve Your Resume")
        for tip in result["improvements"]:
            st.info(f"→ {tip}")
        
        # Summary
        st.subheader("📝 AI Summary")
        st.write(result["summary"])