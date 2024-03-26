import streamlit as st
from hugchat import hugchat
from hugchat.login import Login


st.set_page_config(page_title="talk to yourself")

# H-Face Credentials
with st.sidebar:
    st.title('talking2yourself')
    if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
        st.success('HuggingFace Login credentials already provided!', icon='✅')
        hf_email = st.secrets['EMAIL']
        hf_pass = st.secrets['PASS']
    else:
        hf_email = st.text_input('Enter e-mail:', type='password')
        hf_pass = st.text_input('Enter password:', type='password')
        if not (hf_email and hf_pass):
            st.warning('log in with hugging-face account', icon='⚠️')
        else:
            st.success('prompt me, bro', icon='👉')
    
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "log in and then ask me whatever you want"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def generate_response(prompt_input, email, passwd):
    # H-Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # new chatbot spawn                        
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# generate response if last message not from assistant

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, hf_email, hf_pass) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)