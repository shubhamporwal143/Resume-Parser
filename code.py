import docx
import PyPDF2
import re
import nltk

def resume(file_path):
    
    #for .pdf files
    if file_path.lower().endswith('.pdf'):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()

    #for .docx files
    elif file_path.lower().endswith('.docx'):
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        text = '\n'.join(full_text)

    else:
        print("Unsupported file format")
        return None


    # Extract name
    n_pattern = re.compile(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b")
    n_matches = n_pattern.findall(text)
    if n_matches:
        name = n_matches[0]

    # Extract email
    em_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    em_matches = em_pattern.findall(text)
    if em_matches:
        email = em_matches[0]

    # Extract phone number
    ph_pattern = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
    ph_matches = ph_pattern.findall(text)
    if ph_matches:
        phone = ph_matches[0]

    # Extract education details
    ed_pattern = re.compile(r"\bEducation\b(.+?)\bProjects\b", re.DOTALL | re.IGNORECASE)
    ed_matches = ed_pattern.findall(text)
    
    if ed_matches:
        ed_text = ed_matches[0]
        education = [line.strip() for line in ed_text.split('\n') if line.strip()]

    # Extract experience
    exp_pattern = re.compile(r"\bWork Experience\b(.+?)\bSkills\b", re.DOTALL | re.IGNORECASE)
    exp_matches = exp_pattern.findall(text)
    if exp_matches:
        exp_text = exp_matches[0]
        experience = [line.strip() for line in exp_text.split('\n') if line.strip()]
    
    #Extract skills 
    nltk.download('stopwords')
    skill_ls = ['machine learning','data science','C++','html','css','angular','react','java','computer vision','django','python','excel','english']
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(text)
 
    filtered_tokens = [w for w in word_tokens if w not in stop_words]
    filtered_tokens = [w for w in word_tokens if w.isalpha()]
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
    found_skills = set()
    for token in filtered_tokens:
        if token.lower() in skill_ls:
            found_skills.add(token)

    for ngram in bigrams_trigrams:
        if ngram.lower() in skill_ls:
            found_skills.add(ngram)
    skills = list(found_skills)

    resume_data = {
        'Name': name,
        'Email': email,
        'Phone': phone,
        'Education': education,
        'Experience': experience,
        'Skills': skills,
    }
    return resume_data


#main
import json
resume_file = input("enter path of resume: ")
parsed_resume = resume(resume_file)
if parsed_resume:
    json_file_path = "parsed_resume.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(parsed_resume, json_file, indent=4)