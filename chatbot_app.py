import streamlit as st

st.set_page_config(page_title="Simple Chatbot", page_icon="💬")

st.title("💬 Simple Chatbot Demo")
st.write("Selamat datang di chatbot demo sederhana ini! Ketik pesan Anda di bawah, dan bot akan membalas (dummy response). ")

with st.sidebar:
    st.header("Tentang Aplikasi")
    st.write("""
    🤖 Chatbot sederhana dibuat dengan Python + Streamlit.
             
    Karena belum ada koneksi ke OpenAI APPI, bot hanya membalas echo pesan anda.
             """)
    

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previus messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# User input
user_input = st.chat_input("Ketik pesan Anda...")

if user_input:
    # Simulate bot response
    bot_reply = f"Echo: {user_input}"

    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Add bot reply
    st.session_state.messages.append({"role": "user", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
