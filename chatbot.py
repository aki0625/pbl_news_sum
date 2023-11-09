import streamlit as st
st.set_page_config(
    page_title="愛媛新聞要約アプリ",
    page_icon="🤗"
)
st.header("愛媛新聞要約アプリ 🤗")

if user_input := st.chat_input("要約したい記事の内容を入力してね！"):
    # なにか入力されればここが実行される
    with st.spinner("ChatGPT is typing ..."):
        response = llm(st.session_state.messages)
