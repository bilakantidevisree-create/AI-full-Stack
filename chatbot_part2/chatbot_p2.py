from ollama import chat
import streamlit as st
st.set_page_config(page_title = "App",page_icon="🐻")
st.title("App - Here to talk!")


personality = " You are friendly and patient tutor named Llama.ANswer warmly.Keep the answers within one sentence."
personality_2 = "You are a strict and impatient tutor named llama.Answer shortly and strictly.keep the answers within one sentemce."

if "history" not in st.session_state:
    st.session_state.history = None 
if st.session_state.toast_msg:
    st.toast(st.session_state.toast_msg[0], st.session_state.toast_msg[1])
    st.session_state.toast_msg = None
with st.sidebar:
    st.header("chat controls")
    if st.button("Clear chat",type = "primary"):
        st.session_state.history = [{"role" : "system","content" : personality}]
        st.session_state.toast_msg = ("chat cleared successfully","success")
        st.rerun()
    if st.button("change personality"):
        st.session_state.history[0]["content"] = personality_2
        st.session_state.toast_msg = ("Bot personality changed successfully!","success") 
        st.rerun()

with st.chat_message("assistant"):
    st.write("Hello! I'm Llma.Ask something to get started.")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Type something...")
if question:
    st.session_state.history.append({"role" : "user","content" : question})
    with st.chat_message("user"):
        st.write(question)
    try:
        with st.spinner("Thinking..."):
            response = chat(model="llama3.2", messages = st.session_state.history)
        reply = response["message"]["content"]
        st.session_state.history.append({"role": "assistant","content":reply})

        with st.chat_message("assistant"):
            st.write(reply)
    except Exception as e:
        st.write("ollama is not working.Try again later.")
