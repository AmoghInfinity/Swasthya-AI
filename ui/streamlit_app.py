import sys
import os

# Import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.graph import graph
from app.rag import load_documents

# Load Knowledge Base
if "kb_loaded" not in st.session_state:
    load_documents()
    st.session_state.kb_loaded = True

# Page Config
st.set_page_config(page_title="SwasthyaAI", layout="wide")

# UI Styling
st.markdown("""
<style>

/* Buttons */
.stButton>button {
    background-color: white !important;
    color: black !important;
    border: 2px solid black !important;
    border-radius: 10px !important;
    height: 45px;
    width: 100%;
    font-weight: bold;
}

/* Hover */
.stButton>button:hover {
    background-color: #f3f4f6 !important;
    color: black !important;
}

/* Focus / Click */
.stButton>button:focus,
.stButton>button:active {
    color: black !important;
    background-color: #e5e7eb !important;
    border: 2px solid black !important;
}

/* Fix hidden text issue */
.stButton button span {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>SwasthyaAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>AI-powered Health & Diet Assistant</p>", unsafe_allow_html=True)

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input Section
col1, col2 = st.columns([9, 1])

with col1:
    user_input = st.text_input(
        "Ask your health question...",
        placeholder="e.g. Protein veg diet",
        label_visibility="collapsed"
    )

with col2:
    submit = st.button("➤", use_container_width=True)

# Process Query
if submit and user_input:
    state = {
        "question": user_input,
        "messages": st.session_state.messages,
        "eval_retries": 0
    }

    with st.spinner("Analyzing your query..."):
        result = graph.invoke(state)

    answer = result["answer"]

    # Store messages in correct format
    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("ai", answer))

# Display Chat
for item in st.session_state.messages:
    if isinstance(item, tuple) and len(item) == 2:
        role, msg = item
        if role == "user":
            st.markdown(f"<div class='chat-user'><b>You:</b> {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-ai'><b>AI:</b><br>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-ai'>{item}</div>", unsafe_allow_html=True)

# Clear Chat
if st.button("Clear Chat"):
    st.session_state.messages = []