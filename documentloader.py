import PyPDF2
import io

def load_document(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()

    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    
    else:
        return "Unsupported file format."
