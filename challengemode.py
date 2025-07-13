import random

def generate_challenge_questions(text):
    # Very basic logic-based question template
    questions = [
        "Summarize the main project described in the document.",
        "What problem was addressed and how?",
        "Identify any outcome or result mentioned.",
        "Who were the key collaborators or stakeholders?",
        "Which tools or techniques were used?"
    ]
    return random.sample(questions, 3)

def evaluate_user_response(user_answer, correct_context_snippet):
    if user_answer.strip().lower() in correct_context_snippet.lower():
        return "✅ Correct", correct_context_snippet
    else:
        return "❌ Incomplete or incorrect", correct_context_snippet
