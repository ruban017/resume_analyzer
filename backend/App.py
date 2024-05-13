import pdfplumber
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load nltk stopwords
nltk.download('punkt')
nltk.download('stopwords')

# Load the PDF file
def parse_resume(file_path):
    with pdfplumber.open(file_path) as pdf:
        resume_text = ""
        for page in pdf.pages:
            resume_text += page.extract_text()
    return resume_text

# Preprocess text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    return [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]

# Sample job description
job_description = "We are looking for a software engineer proficient in Python and Java with experience in web development."

# Sample PDF resume file path
resume_file_path = "sample_resume.pdf"

# Parse resume text from the PDF file
resume_text = parse_resume(resume_file_path)

# Preprocess job description and resume text
job_description_processed = ' '.join(preprocess_text(job_description))
resume_text_processed = ' '.join(preprocess_text(resume_text))

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
job_vector = vectorizer.fit_transform([job_description_processed])
resume_vector = vectorizer.transform([resume_text_processed])

# Calculate cosine similarity
cosine_sim = cosine_similarity(job_vector, resume_vector)

# Define threshold and calculate ATS score
threshold = 0.5  # You can adjust this threshold as needed
ats_score = cosine_sim[0][0] * 100 if cosine_sim[0][0] >= threshold else 0

print("Cosine Similarity:", cosine_sim[0][0])
print("ATS Score:", ats_score)
