from transformers import pipeline
import textwrap

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def split_text(text, max_chunk_length=1000):
    """
    Splits long text into manageable chunks for the summarizer.
    """
    paragraphs = text.split('\n')
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) < max_chunk_length:
            current_chunk += " " + para.strip()
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para.strip()
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks


def summarize_text(text):
    chunks = split_text(text)
    full_summary = ""

    for chunk in chunks[:5]:  # summarize only first 5 chunks to save API/token cost
        if chunk.strip():
            try:
                summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
                full_summary += summary + " "
            except Exception as e:
                print("Summarization error:", e)
                continue

    # Trim final summary to ≈150 words (requirement)
    word_limit = 150
    trimmed_summary = ' '.join(full_summary.split()[:word_limit])
    return trimmed_summary
