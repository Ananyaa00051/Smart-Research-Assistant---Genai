from transformers import pipeline

# Load the QA pipeline once with an optimized model
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_question(question, context):
    """
    Answers a question using the provided context.
    Returns: answer, confidence_score, start_pos, end_pos
    """
    if not context.strip():
        return "No content to search.", 0.0, 0, 0

    try:
        result = qa_pipeline(question=question, context=context)

        answer = result.get("answer", "N/A")
        score = result.get("score", 0.0)
        start = result.get("start", 0)
        end = result.get("end", 0)

        # If boundaries are weird or tiny, fall back gracefully
        if start >= end or len(answer.strip()) == 0:
            return "No valid answer found in the document.", 0.0, 0, 0

        return answer.strip(), float(score), int(start), int(end)

    except Exception as e:
        print("❌ QA Engine Error:", e)
        return "Unable to answer that based on the document.", 0.0, 0, 0

