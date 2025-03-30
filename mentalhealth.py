import streamlit as st
import google.generativeai as geimport streamlit as st
import google.generativeai as genai
import os

# Set up API key securely (Replace with your own key)
API_KEY = "AIzaSyCX5TKAFYkpT3JLnEa0_alXNjwYpe_-S2E"  # Do not share this key publicly!
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit UI
st.title("💙 Mental Health Support Chatbot")
st.write("Hello! I'm here to listen and support you. Feel free to share your thoughts, and I'll try my best to help. Remember, you're not alone! 💙")

# Initialize session state for chat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("How are you feeling today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate empathetic response
    try:
        response = st.session_state.chat.send_message(
            f"You are a mental health support chatbot. Provide a caring, empathetic, and supportive response to: {prompt}. Offer encouragement and self-care tips."
        )
        response_text = response.text
    except Exception as e:
        response_text = "I'm here for you, but I'm facing some technical issues right now. Please try again later. 💙"

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)

    # Encourage seeking professional help for serious concerns
    if any(word in prompt.lower() for word in ["depressed", "anxious", "hopeless", "overwhelmed", "suicidal"]):
        follow_up = "💡 If you're struggling, please consider reaching out to a trusted friend, family member, or a mental health professional. You are not alone. 💙"
        st.session_state.messages.append({"role": "assistant", "content": follow_up})
        with st.chat_message("assistant"):
            st.markdown(follow_up)nai
import os

# Set up API key securely (Replace with your own key)
API_KEY = "AIzaSyCX5TKAFYkpT3JLnEa0_alXNjwYpe_-S2E"  # Do not share this key publicly!
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')
import streamlit as st
import google.generativeai as genai
import os

# Set up API key securely (Replace with your own key)
API_KEY = "YOUR_API_KEY_HERE"  # Do not share this key publicly!

genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .title {
            font-size: 36px;
            color: #3A5A98;
            text-align: center;
            font-weight: bold;
        }
        .subtitle {
            font-size: 18px;
            color: #444;
            text-align: center;
            margin-bottom: 20px;
        }
        .chat-container {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 700px;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

# UI Header
st.markdown('<p class="title">💙 Mental Health Support Chatbot</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">"You are not alone. Let's talk and feel better together. 💙"</p>', unsafe_allow_html=True)

# Initialize session state for chat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown('</div>', unsafe_allow_html=True)

# Get user input
if prompt := st.chat_input("💭 How are you feeling today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate empathetic response
    try:
        response = st.session_state.chat.send_message(
            f"You are a mental health support chatbot. Provide a caring, empathetic, and supportive response to: {prompt}. Offer encouragement and self-care tips."
        )
        response_text = response.text
    except Exception as e:
        response_text = "I'm here for you, but I'm facing some technical issues right now. Please try again later. 💙"

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)

    # Encourage seeking professional help for serious concerns
    if any(word in prompt.lower() for word in ["depressed", "anxious", "hopeless", "overwhelmed", "suicidal"]):
        follow_up = "💡 If you're struggling, please consider reaching out to a trusted friend, family member, or a mental health professional. You are not alone. 💙"
        st.session_state.messages.append({"role": "assistant", "content": follow_up})
        with st.chat_message("assistant"):
            st.markdown(follow_up)

# Streamlit UI
st.title("💙 Mental Health Support Chatbot")
st.write("Hello! I'm here to listen and support you. Feel free to share your thoughts, and I'll try my best to help. Remember, you're not alone! 💙")

# Initialize session state for chat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("How are you feeling today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate empathetic response
    try:
        response = st.session_state.chat.send_message(
            f"You are a mental health support chatbot. Provide a caring, empathetic, and supportive response to: {prompt}. Offer encouragement and self-care tips."
        )
        response_text = response.text
    except Exception as e:
        response_text = "I'm here for you, but I'm facing some technical issues right now. Please try again later. 💙"

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)

    # Encourage seeking professional help for serious concerns
    if any(word in prompt.lower() for word in ["depressed", "anxious", "hopeless", "overwhelmed", "suicidal"]):
        follow_up = "💡 If you're struggling, please consider reaching out to a trusted friend, family member, or a mental health professional. You are not alone. 💙"
        st.session_state.messages.append({"role": "assistant", "content": follow_up})
        with st.chat_message("assistant"):
            st.markdown(follow_up)
