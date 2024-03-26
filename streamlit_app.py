import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title="talking to myself - an open source LLM app")

with st.sidebar:
    st.title('ask_again')
    add_vertical_space(5)
    st.markdown('''
   an LLM-powered chatbot, built using [streamlit](<https://streamlit.io/>) and [hugchat](<https://github.com/Soulter/hugging-chat-api>)
    ''')
    add_vertical_space(15)
    st.write('thrown together by [Бог](<https://www.boag.dev>)')
    
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["I'm HugChat, How may I help you?"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ['Hi!']
