# Resume-Parser
README
Resume Parser
The Resume Parser is a Python script that extracts important information from resumes in either .docx or .pdf format. It identifies and extracts details such as name, email, phone number, education, experience, and relevant skills.
Approach
•	Check whether the format is correct or not.
•	Used regular expressions and NLP  for extracting names, phone numbers, etc.
•	Used predefined ‘skills_ls’ database for extracting skills.
•	Used JSON library for saving the parsed data in JSON format.
Requirements
Before running the script, make sure you have the following installed:
•	Python 3.x
•	Python libraries: docx, PyPDF2, nltk, JSON, re.
Supported formats
•	Save the resume you want to parse in either .docx or .pdf format.
Limited Skills parsing
The script uses a predefined skills database (skill_ls) to identify relevant skills in the resume. The skills database is defined as:
skill_ls = ['machine learning', 'data science', 'C++', 'html', 'css', 'angular', 'react', 'java', 'computer vision', 'django', 'python', 'excel', 'english'] 
Steps:
1.	Download all the above-mentioned requirements using pip or pip3.
2.	Copy the link of the project.
3.	Open terminal or cmd 
4.	(optional) change path if you want to save project in different directory
5.	Now type “git clone # follow up with the copied link”
6.	Press enter
7.	Type “cd # project name”
8.	Type “python or python3 resume_parser.py”
9.	Now give the path where the resume is present  as an input
10.	Press enter 
11.	The extracted data is stored in the same directory in parsed_resume.json

Pros/Cons
•	Result may vary with different templates of the resume
•	The script uses regular expressions and simple heuristics to extract information, which may not be 100% accurate. Manual review and validation of the parsed data may be necessary.
•	The skills identification process is based on the presence of keywords in the resume. It may not capture all skills accurately, and false positives may occur.
•	This would be usefull for filtering resume according to the recruiter’s needs.

