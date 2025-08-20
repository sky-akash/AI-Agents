import streamlit as st
from langchain_core.messages import HumanMessage

# lets import chatbot
from langgraph_chat_backend import chatbot                         # how we imported a variable ? object ? we can if it is at top level

import uuid            # helps to generate random id

####################### Utility function 1 #######################

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id            # generates a random thread id, now we have to add it to the session setup

# defining the config
# CONFIG = {'configurable': {'thread_id': 'thread-1'}}

############################################### Session Setup ##############################################
# st,session_state :) a dict
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = [] 

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id() # if not generatea then generating a thread id

# need to store history in a dictionary

# message_history = []

############ starting with sidebar

st.sidebar.title("Gemini pe aadharit LangGrapgh ka chatbot")

st.sidebar.button("Nayi Kahani?")

st.sidebar.header("Humari Baatcheet")

st.sidebar.text(st.session_state['thread_id'])
############################################### Main Code ##############################################

# loading conv. history
for message in st.session_state['message_history']:                              # message_history
    with st.chat_message(message['role']):
        st.text(message['content'])

# ('role':'user', 'content': 'Hi')
# ('role':'assistant', 'content': 'Helloooooo')

user_input = st.chat_input('Type Here')

if user_input:

    # add message to dict
    # message_history.append({'role':'user', 'content': user_input})
    st.session_state['message_history'].append({'role':'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(     # python generator
                {'messages': [HumanMessage(content=user_input)]},
                config = CONFIG,
                stream_mode = 'messages'
            )
        )

    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})


###############################################  ##############################################

# Need to replace invoke with stream :)
    # response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=config)       # need input as initial state 
    # ai_message = response['messages'][-1].content

    # st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})
    # with st.chat_message('asistant'):
    #     st.text(ai_message)

    # # st.session_state['message_history'].append({'role':'assistant', 'content': user_input})
    # # with st.chat_message('asistant'):
    # #     st.text(user_input)



#  # main cmponents
# # 1. message display box -> chat_message
# # 2. input box -> chat_input

# with st.chat_message('user'):
#     st.text('Hi')

# with st.chat_message('assistant'):
#     st.text('How can I help you today?')

# user_input = st.chat_input('Type Here')

# if user_input:
#     with st.chat_message('user'):
#         st.text(user_input)

                    # import streamlit as st


                    # # st,session_state :) a dict

                    # if 'message_history' not in st.session_state:
                    #     st.session_state['message_history'] = [] 

                    # # need to store history in a dictionary

                    # # message_history = []

                    # # loading conv. history
                    # for message in st.session_state['message_history']:                              # message_history
                    #     with st.chat_message(message['role']):
                    #         st.text(message['content'])

                    # # ('role':'user', 'content': 'Hi')
                    # # ('role':'assistant', 'content': 'Helloooooo')

                    # user_input = st.chat_input('Type Here')

                    # if user_input:

                    #     # add message to dict
                    #     # message_history.append({'role':'user', 'content': user_input})
                    #     st.session_state['message_history'].append({'role':'user', 'content': user_input})
                    #     with st.chat_message('user'):
                    #         st.text(user_input)

                    #     st.session_state['message_history'].append({'role':'assistant', 'content': user_input})
                    #     with st.chat_message('asistant'):
                    #         st.text(user_input)



#  # main cmponents
# # 1. message display box -> chat_message
# # 2. input box -> chat_input

# with st.chat_message('user'):
#     st.text('Hi')

# with st.chat_message('assistant'):
#     st.text('How can I help you today?')

# user_input = st.chat_input('Type Here')

# if user_input:
#     with st.chat_message('user'):
#         st.text(user_input)

