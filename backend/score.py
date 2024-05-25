import pdfplumber
import re
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
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

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    return [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]

def extract_skill_section(resume_text):
    start_pattern = r'\b(SKILLS|TECHNICAL SKILLS|KEY COMPETENCIES|PROFESSIONAL SKILLS)\b'
    end_pattern = r'\b(PROJECTS|EXPERIENCE|WORK EXPERIENCE|EDUCATION|INTERNSHIP|LANGUAGE FLUENCY|CERTIFICATIONS|AWARDS|ACHIEVEMENTS)\b'
    
    start_match = re.search(start_pattern, resume_text, re.IGNORECASE)
    
    if start_match:
        start_position = start_match.end()
        end_match = re.search(end_pattern, resume_text[start_position:], re.IGNORECASE)
        
        if end_match:
            end_position = start_position + end_match.start()
            skill_section = resume_text[start_position:end_position]
            skill_section.strip()
            return skill_section
    
    return None

def project_section(resume_text):
    start_pattern = r'\b(PROJECTS|WORK EXPERIENCE|INTERNSHIPS|EXPERIENCE)\b'
    end_pattern = r'\b(EDUCATION|LANGUAGE FLUENCY|CERTIFICATIONS|AWARDS|ACHIEVEMENTS|SKILLS)\b'
    
    start_match = re.search(start_pattern, resume_text, re.IGNORECASE)
    
    if start_match:
        start_position = start_match.end()
        end_match = re.search(end_pattern, resume_text[start_position:], re.IGNORECASE)
        
        if end_match:
            end_position = start_position + end_match.start()
            proj_section = resume_text[start_position:end_position]
            proj_section.strip()
            return proj_section
    return None

def create_doughnut_chart(n):
    single_value = n
    remaining_value = 100.00000000000003 - single_value

    sizes = [single_value, remaining_value]
    colors = ['#FFA500', '#FF0000']   

    fig, ax = plt.subplots()
    ax.pie(sizes, colors=colors, wedgeprops=dict(width=0.3), startangle=90)
    plt.text(0, 0, f'{single_value:.3f}%', ha='center', va='center', fontsize=20, weight='bold')

    ax.axis('equal')

    plt.savefig('doughnut_chart.png', bbox_inches='tight', pad_inches=0.1, transparent=True)
    plt.close(fig)

def analyze_resume(file_path, job_description):
    resume_text = parse_resume(file_path)
    skill_section = extract_skill_section(resume_text)
    proj_section = project_section(resume_text)
    # skill_section+=proj_section
    skill_section = resume_text
    # print(skill_section)
    
    if skill_section:
        job_description_processed = ' '.join(preprocess_text(job_description))
        resume_text_processed = ' '.join(preprocess_text(skill_section))
        
        vectorizer = TfidfVectorizer()
        job_vector = vectorizer.fit_transform([job_description_processed])
        resume_vector = vectorizer.transform([resume_text_processed])
        
        cosine_sim = cosine_similarity(job_vector, resume_vector)
        
        threshold = 0.1
        ats_score = cosine_sim[0][0] * 100 if cosine_sim[0][0] >= threshold else 0
        
        print(ats_score)
        # return ats_score
        create_doughnut_chart(ats_score)
    else:
        return 0
# analyze_resume("CIT_Rubankumar_AI&DS.pdf","numpy")
