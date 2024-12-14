from PyPDF2 import PdfReader
from docx import Document
import openai
from nltk.tokenize import sent_tokenize
import os
import time


openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text(file):
    """
    Args:
        file: Input File Uploaded

    Returns:
        Contents of the file
    """
    if file.type == "application/pdf":
        pdf_reader = PdfReader(file)
        text = " ".join(page.extract_text() for page in pdf_reader.pages)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
    else:
        text = file.read().decode("utf-8")
    return text


def chunk_text(text, max_tokens=3000):
    """
    Args:
        text: Contents fetched from the input file
        max_tokens: Max token at once

    Returns:
        Chunks of texts
    """
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence_length = len(sentence.split())
        if current_length + sentence_length > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0

        current_chunk.append(sentence)
        current_length += sentence_length

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# def generate_user_stories_and_criteria(text):
#     """
#     Args:
#         text: Contents of the input file

#     Returns:
#         Generated user stories and acceptance criteria from the model.
#     """
#     chunks = chunk_text(text)
#     user_stories = []


#     for chunk in chunks:
#         messages = [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f'''Based on the following requirements:
#              {chunk}
#             Generate user stories and acceptance criteria for each requirement.'''}
#         ]
#         response = openai.ChatCompletion.create(
#         model="gpt-4o",
#         messages=messages,
#         max_tokens=1500,
#         temperature=0
#         )
#         user_stories.append(response.choices[0].message['content'].strip())

#     return "".join(user_stories)

def generate_user_stories_and_criteria_specific(text):
    """
    Args:
        text: Contents of the input file

    Returns:
        Generated user stories and acceptance criteria from the model.
    """
    chunks = chunk_text(text)
    user_stories = []
    for chunk in chunks:
        prompt = f"""
                You are tasked with creating User Stories and Acceptance Criteria from the given document. 
                {chunk}
                Follow these instructions:
                
    
                1. Identify all **Modules** in the document (e.g., Recruitment & Onboarding, Attendance, Leave Management, etc.).
                2. For each module, extract individual **User Stories** based on the functionalities described.
                3. For each User Story:
                   - Assign a **User Story Title** that reflects the functionality.
                   - Define the **Roles** involved (e.g., HR, Recruiter, Employee, Manager).
                   - List the **Actions** that each role can perform under the User Story.
                   - For each action, specify the **arguments** required (e.g., fields like title, description, date).
                
                Use the following format for each module:
                
                Module Name: [Module Name]
                User Story [X]: [User Story Title]
                Acceptance Criteria:
                Role: [Role Name]
                - [Action 1]
                  arguments: [Argument 1, Argument 2, ...]
                - [Action 2]
                  arguments: [Argument 1, Argument 2, ...]
                
                Role: [Role Name]
                - [Action 1]
                  arguments: [Argument 1, Argument 2, ...]
                - [Action 2]
                  arguments: [Argument 1, Argument 2, ...]
                
                Ensure the output is structured and consistent. Generate one User Story for each identified functionality under the module, clearly distinguishing between roles and their actions.
                
                Example:
                
                Module Name: Recruitment & Onboarding
                User Story 1: Job Postings
                Acceptance Criteria:
                Role: Recruiter
                - create job
                  arguments: title, description, requirements
                - edit job
                  arguments: title, description, requirements
                
                Role: Candidate
                - view jobs
                  arguments: filters (location, role, etc.)
                - apply for jobs
                  arguments: resume, cover letter
        """
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt.strip()}
        ]
        response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1500,
        temperature=0
        )
        user_stories.append(response.choices[0].message['content'].strip())

    return "".join(user_stories)


