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
        
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()




def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
with input_container:
    user_input = get_text()
    
def generate_response(prompt):
    chatbot = hugchat.ChatBot()
    response = chatbot.chat(prompt)
    return response


with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))