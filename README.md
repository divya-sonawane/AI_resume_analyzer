# 🧠 AI Resume Analyzer & Job Matcher

An intelligent resume analysis tool powered by Google Gemini AI that compares your resume against job descriptions, provides match scores, identifies skill gaps, and offers personalized improvement suggestions.

## ✨ Features

- **PDF Resume Upload**: Seamlessly upload your resume in PDF format
- **Job Description Matching**: Paste any job description for comparison
- **AI-Powered Analysis**: Uses Google Gemini 2.0 Flash to analyze resume-job fit
- **Match Score**: Get a percentage score (0-100%) indicating resume compatibility
- **Skill Analysis**: 
  - Matched skills highlighting what you already have
  - Missing skills showing what you need to learn
- **Personalized Recommendations**: AI-generated improvement suggestions
- **Executive Summary**: Get an AI-powered overview of your resume fit
- **Interactive UI**: Beautiful Streamlit interface with color-coded results

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/divya-sonawane/resume-analyzer.git
   cd resume-analyzer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your-google-gemini-api-key-here
   ```

   **How to get your Gemini API key:**
   - Visit [Google AI Studio](https://aistudio.google.com/apikey)
   - Click "Get API Key"
   - Create a new API key
   - Copy and paste it into your `.env` file

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

   The app will open in your browser at `http://localhost:8501`

## 📖 How to Use

1. **Upload Your Resume**
   - Click the file uploader on the left side
   - Select your resume in PDF format

2. **Paste Job Description**
   - Copy a job description from any job posting
   - Paste it into the text area on the right side

3. **Click "Analyze Resume"**
   - The AI will process your resume against the job description
   - Wait for the analysis to complete

4. **Review Results**
   - **Match Score**: Visual percentage with color coding (green: 70%+, orange: 40-70%, red: <40%)
   - **Matched Skills**: Skills from your resume that match the job
   - **Missing Skills**: Skills you should consider learning
   - **Improvement Tips**: Actionable suggestions to improve your resume
   - **AI Summary**: Detailed analysis of your fit for the role

## 📁 Project Structure

```
resume-analyzer/
├── app.py                 # Main Streamlit application
├── utils.py              # Helper functions (PDF extraction, AI analysis)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not in git)
└── README.md            # This file
```

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Interactive web framework for data apps
- **[Google Gemini API](https://ai.google.dev/)** - Advanced AI model for resume analysis
- **[PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)** - PDF text extraction
- **[python-dotenv](https://python-dotenv.readthedocs.io/)** - Environment variable management

## 📋 Dependencies

See [requirements.txt](requirements.txt) for the complete list:
- `streamlit` - Web interface
- `pymupdf` - PDF processing
- `google.generativeai` - Google Gemini API
- `python-dotenv` - Environment configuration
- `openai` - (optional, for future extensions)

## 🔧 Configuration

### Customizing the Analysis

Edit the `prompt` in `utils.py` (in the `analyze_resume()` function) to:
- Change the analysis criteria
- Add or remove fields in the JSON response
- Adjust the analysis depth

### Adjusting Match Score Colors

In `app.py`, modify the color thresholds:
```python
color = "green" if score >= 70 else ("orange" if score >= 40 else "red")
```

## 💡 Tips for Best Results

1. **Resume Format**: Use clear, well-structured PDFs for accurate text extraction
2. **Job Description**: Include the full job description, not just the title
3. **Keywords**: Ensure your resume uses the same terminology as the job posting
4. **Multiple Applications**: Try with different job descriptions to identify skill gaps
5. **Regular Updates**: Regularly update your resume based on recommendations

## 🐛 Troubleshooting

### Error: "GEMINI_API_KEY not found"
- Ensure `.env` file exists in the project root
- Verify the key name is exactly `GEMINI_API_KEY`
- Restart the Streamlit app after creating `.env`

### Error: "Repository not found" on git push
- Ensure you've created the repository on GitHub
- Verify the repository URL in git config: `git remote -v`
- Use correct authentication (SSH or Personal Access Token)

### PDF Extract Issues
- Ensure the PDF is readable and not corrupted
- Try opening the PDF in Adobe Reader
- Avoid scanned image PDFs if possible

### Streamlit Connection Issues
- Check your internet connection
- Verify Gemini API key is valid
- Check your Google account quota/billing

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Divya Sonawane**
- GitHub: [@divya-sonawane](https://github.com/divya-sonawane)

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) for powerful AI analysis
- [Streamlit](https://streamlit.io/) for the excellent web framework
- [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF handling


---

**Happy Resume Analyzing! 🚀**
