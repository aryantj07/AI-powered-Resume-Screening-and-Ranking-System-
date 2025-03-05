# AI-powered-Resume-Screening-and-Ranking-System-
🚀 Efficient AI-driven Resume Analysis and Candidate Ranking

📌 Project Overview
This project is an AI-powered system that automates resume screening by extracting text from PDF resumes and ranking candidates based on a given job description. Using Natural Language Processing (NLP) and Machine Learning, it simplifies the hiring process by providing an objective ranking of applicants.

🌟 Key Features
✔ Automated Resume Parsing – Extracts text from uploaded resumes
✔ AI-Based Ranking – Uses TF-IDF and Cosine Similarity for evaluation
✔ Adjustable Weighting – Customize ranking based on skill and experience importance
✔ Keyword Highlighting – Identifies key skills from job descriptions
✔ Data Visualization – Graphical representation of ranking results
✔ CSV Export – Download ranking results for further review

🛠 Technology Stack
🔹 Frontend: Streamlit
🔹 Backend: Python, Scikit-learn, pdfplumber
🔹 NLP Techniques: TF-IDF, Cosine Similarity
🔹 Data Processing & Visualization: Pandas, Matplotlib

📂 Project Structure
📦 AI-Resume-Screening
│── 📂 sample_resumes/      # Sample resumes for testing
│── 📂 screenshots/         # UI snapshots
│── 📂 docs/                # Project documentation and reports
│── 📜 app.py               # Main application script
│── 📜 requirements.txt      # List of dependencies
│── 📜 README.md            # Project documentation

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/your-username/AI-Resume-Screening.git
cd AI-Resume-Screening
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
streamlit run app.py

📸 Screenshots
1️⃣ Home Page – Interface for entering the job description and uploading resumes.
2️⃣ Upload Section – Displays uploaded resumes and job description input.
3️⃣ Ranked Table – Shows resumes ranked based on similarity scores.
4️⃣ Graphical Insights – Bar chart visualizing candidate scores.
5️⃣ Top Resume Highlights – Dropdown to view key details with highlighted keywords.
6️⃣ Download Results – Option to download ranking results as a CSV file.
7️⃣ CSV Output – Displays the final ranked resume results in a structured format.

🔮 Future Enhancements
🚀 Integrate deep learning models (e.g., BERT, GPT) for better ranking
🚀 Enhance bias detection and fairness in evaluation
🚀 Improve UI for better user interaction
🚀 Extend functionality with Applicant Tracking System (ATS) integration

📌 Conclusion
This AI-powered resume screening system streamlines the hiring process by ranking candidates based on job relevance. With automated text extraction, similarity scoring, and visual insights, it enhances efficiency and decision-making. The tool simplifies resume evaluation, providing recruiters with structured results for better hiring outcomes.
