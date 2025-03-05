import streamlit as st
import pdfplumber
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from io import BytesIO

def extract_text_from_pdf(file):
    """Extract text from a PDF using pdfplumber."""
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def rank_resumes(job_description, resumes, weight_skills=1.0, weight_experience=1.0):
    """Rank resumes based on job description with weight settings."""
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    job_vector = vectors[0]
    resume_vectors = vectors[1:]
    scores = cosine_similarity([job_vector], resume_vectors).flatten()
    
    # Adjust scores based on weights (dummy adjustment for now)
    scores = scores * weight_skills * weight_experience
    return scores

def highlight_keywords(text, keywords):
    """Highlight keywords from job description in resumes."""
    for keyword in keywords:
        text = re.sub(f'(?i)\b{re.escape(keyword)}\b', f'**{keyword}**', text)
    return text

def generate_download_link(df):
    """Generate a download link for CSV export."""
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return output

# Streamlit UI
st.title("AI Resume Screening & Candidate Ranking System")

# Job description input
st.header("Job Description")
job_description = st.text_area("Enter the job description")

# Custom weight settings
st.sidebar.header("Customize Ranking Weights")
weight_skills = st.sidebar.slider("Skill Weight", 0.5, 2.0, 1.0)
weight_experience = st.sidebar.slider("Experience Weight", 0.5, 2.0, 1.0)

# File uploader
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("Ranking Resumes")
    resumes = [extract_text_from_pdf(file) for file in uploaded_files]
    
    # Extract keywords from job description
    job_keywords = job_description.split()
    
    # Rank resumes
    scores = rank_resumes(job_description, resumes, weight_skills, weight_experience)
    
    # Display results
    results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
    results = results.sort_values(by="Score", ascending=False)
    st.write(results)
    
    # Bar chart for visualization
    st.subheader("Candidate Score Distribution")
    fig, ax = plt.subplots()
    ax.barh(results["Resume"], results["Score"], color='skyblue')
    ax.set_xlabel("Score")
    ax.set_ylabel("Candidate")
    ax.set_title("Resume Ranking Scores")
    st.pyplot(fig)
    
    # Highlight keywords in top resumes
    st.subheader("Top Resume Highlights")
    for i, row in results.iterrows():
        resume_text = extract_text_from_pdf(uploaded_files[i])
        highlighted_resume = highlight_keywords(resume_text, job_keywords)
        with st.expander(f"{row['Resume']} - Score: {row['Score']:.2f}"):
            st.markdown(highlighted_resume)
    
    # CSV Download
    st.download_button("Download Results as CSV", generate_download_link(results), "resume_rankings.csv", "text/csv")
