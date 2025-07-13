import streamlit as st
from documentloader import load_document
from summarizer import summarize_text
from qaengine import answer_question
from challengemode import generate_challenge_questions, evaluate_user_response
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Enable chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit setup
st.set_page_config(
    page_title="📄 Smart Research Assistant",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS with background image & improved contrast
st.markdown("""
    <style>
        .stApp {
            background-image: url('https://media.istockphoto.com/id/1172956424/photo/3d-abstract-sculptural-geometric-shapes-background.jpg?s=612x612&w=0&k=20&c=O4K8W7BXw3u32aSIcCE1tOwesPNaMWnpNZ6AyN_avJc=');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }
        .stApp::before {
            content: "";
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background: rgba(255, 255, 255, 0.85);
            z-index: -1;
        }
        .reportview-container {
            padding: 2rem;
        }
        .stButton>button {
            background-color: #004080;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.2em;
            font-weight: bold;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: #000000;
            border-radius: 6px;
            padding: 0.4em;
        }
        .block-container {
            max-width: 900px;
            margin: auto;
        }
        .highlight-box {
            background-color: #eaf4ff;
            padding: 0.75em;
            border-left: 5px solid #0066cc;
            border-radius: 6px;
            margin-top: 0.5em;
            font-size: 0.95rem;
            color: #222222;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🧠 Smart Assistant for Research Summarization")
st.markdown("Upload a structured document and explore intelligent summarization, question-answering, and logic-based assessments.")

# Upload
uploaded_file = st.file_uploader("📤 Upload your research paper, resume, or technical document", type=["pdf", "txt"])

# Document Processing
if uploaded_file:
    raw_text = load_document(uploaded_file)

    # Summary
    st.markdown("---")
    st.subheader("📌 Auto Summary (≤ 150 words)")
    with st.spinner("Generating summary... please wait ⏳"):
        summary = summarize_text(raw_text)
    st.success(summary)

    # QnA
    st.markdown("---")
    st.subheader("💬 Ask Anything from Document")

    user_question = st.text_input("🗣️ Enter your question here:")

    if user_question:
        with st.spinner("Searching the document for the answer..."):
            answer, score, start, end = answer_question(user_question, raw_text)
            context_snippet = raw_text[start:end]
            highlighted = (
                raw_text[max(0, start - 80):start]
                + "**" + raw_text[start:end] + "**"
                + raw_text[end:end + 80]
            )

        # Save interaction
        st.session_state.chat_history.append((user_question, answer))

        st.markdown(f"**✅ Answer:** {answer}")
        st.caption(f"🔍 Confidence Score: {score:.2f}")
        st.markdown(f"<div class='highlight-box'>📎 Justification: \"{context_snippet.strip()}\"</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='highlight-box'>🔦 Highlighted Context: {highlighted.strip()}</div>", unsafe_allow_html=True)

        # Memory display
        if st.session_state.chat_history:
            st.markdown("🧠 **Recent Interactions:**")
            for i, (q, a) in enumerate(reversed(st.session_state.chat_history[-3:]), 1):
                st.markdown(f"{i}. **Q:** _{q}_  \n  **A:** {a}")

    # Challenge Mode
    st.markdown("---")
    st.subheader("🎯 Challenge Me")

    if st.button("🧩 Generate Logic-Based Questions"):
        st.session_state.challenge_questions = generate_challenge_questions(raw_text)
        st.session_state.challenge_answers = {}

    if "challenge_questions" in st.session_state:
        st.markdown("💡 Try answering these logic-based questions:")
        for i, question in enumerate(st.session_state.challenge_questions):
            user_input = st.text_input(f"Q{i+1}: {question}", key=f"q_{i}")
            if user_input:
                feedback, ref = evaluate_user_response(user_input, raw_text)
                st.markdown(f"**🔍 Feedback:** {feedback}")
                st.caption(f"📎 Based on: \"{ref[:200]}...\"")

# Footer
st.markdown("---")
st.caption("🔧 Built with 🤍 by Ananyaa Sharma")
