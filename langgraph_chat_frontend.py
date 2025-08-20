import streamlit as st


# st,session_state :) a dict

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = [] 

# need to store history in a dictionary

# message_history = []

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

    st.session_state['message_history'].append({'role':'assistant', 'content': user_input})
    with st.chat_message('asistant'):
        st.text(user_input)



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

