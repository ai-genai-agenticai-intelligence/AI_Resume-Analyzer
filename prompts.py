# Pass the extracted text into the prompt using an f-strin
PROMPT = """
You are a professional resume analyzer. Your task is to evaluate the provided resume text and provide a detailed analysis of the candidate's qualifications, skills, and experience. Please highlight the strengths and weaknesses of the resume, and suggest areas for improvement. Additionally, provide a summary of the candidate's overall suitability for potential job opportunities based on the information presented in the resume.

Analyze the following resume carefully.
Provide the output in the following format:

1. ATS Score: [Out of 100]
2. Resume Summary
3. Strengths
4. Weaknesses
5. Recommendations for Improvement
6. Overall Suitability for Job Opportunities
7. Additional Comments (if any)
8. Five Interview questions with answers based on the resume

Resume :

{resume}
"""

