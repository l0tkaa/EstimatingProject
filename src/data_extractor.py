# src/data_extractor.py

from docx import Document

def extract_data_from_word(file_path):
    extracted_data = []
    doc = Document(file_path)
    
    for paragraph in doc.paragraphs:
        if '$' in paragraph.text:
            extracted_data.append(paragraph.text.strip())
    
    return extracted_data