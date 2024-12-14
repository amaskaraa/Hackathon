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

def generate_user_stories_and_criteria(text):
    """
    Args:
        text: Contents of the input file

    Returns:
        Generated user stories and acceptance criteria from the model.
    """
    chunks = chunk_text(text)
    user_stories = []


    for chunk in chunks:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'''Based on the following requirements:
             {chunk}
            Generate user stories and acceptance criteria for each requirement.'''}
        ]
        response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1500,
        temperature=0
        )
        user_stories.append(response.choices[0].message['content'].strip())

    return "".join(user_stories)

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
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'''Based on the following requirements:
             {chunk}
             Stakeholders has the role for each document.Generate all the user story and acceptance criteria from the document.
            For Example:
            1. Recruitment & Onboarding
            User Story 1: Job Postings
            As a [role],
                I want to [goal/action],
                So that [reason/outcome].
            
            Acceptance Criteria:
            Role: [role]
                - [action or feature]
                    - arguments: [parameters, if applicable]
                - [another action or feature]
            
            Ensure all user stories are structured similarly and grouped by functional area (if applicable).'''}
        ]
        response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1500,
        temperature=0
        )
        user_stories.append(response.choices[0].message['content'].strip())

    return "".join(user_stories)


