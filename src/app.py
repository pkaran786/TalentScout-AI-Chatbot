import streamlit as st
from chatbot import Chatbot

st.set_page_config(page_title="TalentScout AI", layout="centered")
st.title("🤖 TalentScout AI Hiring Assistant")

# Initialize session state
if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for actions
with st.sidebar:
    if st.button("🗑️ Clear Chat"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# Display chat messages with custom bubbles
for sender, message in st.session_state.chat_history:
    if sender.lower() == "user":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'><b>Bot:</b> {message}</div>", unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.chat_history.append(("User", prompt))
    st.markdown(f"<div class='user-bubble'><b>You:</b> {prompt}</div>", unsafe_allow_html=True)

    # Get bot response
    response = st.session_state.chatbot.process_input(prompt)
    st.session_state.chat_history.append(("Bot", response))
    st.markdown(f"<div class='bot-bubble'><b>Bot:</b> {response}</div>", unsafe_allow_html=True)
