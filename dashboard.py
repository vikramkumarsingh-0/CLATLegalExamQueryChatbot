# dashboard.py
import streamlit as st
from backend import CLATBot
from knowledge_base import knowledge_base

# Initialize Bot
bot = CLATBot(knowledge_base)

# Streamlit UI
st.set_page_config(page_title="CLAT Chatbot", layout="centered")
st.title("🎓 CLAT 2025 Assistant")
st.markdown("Ask me anything about CLAT preparation, syllabus, or cut-offs!")

# User Input
user_query = st.text_input("💬 Your Question:")

if user_query:
    answer = bot.get_best_match(user_query)
    st.markdown(f"**📌 Answer:** {answer}")

# Footer
st.markdown("---")
st.caption("Powered by spaCy + Streamlit | Modular design by Vikram Singh")
