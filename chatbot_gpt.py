import streamlit as st
from openai import OpenAI

# ⬅️ INI HARUS DI PALING ATAS
st.set_page_config(page_title="Chatbot dengan OpenAI", page_icon="🤖")

# Inisialisasi OpenAI client
client = OpenAI(api_key=st.secrets["OPEN_API_KEY"])

st.title("🤖 Chatbot OpenAI")
st.write("Ketik pesan Anda, dan chatbot bertenaga GPT akan membalas.")

with st.sidebar:
    st.header("Tentang")
    st.write("Chatbot ini menggunakan OpenAI GPT untuk membalas pesan Anda secara cerdas.")

# Inisialisasi riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Anda adalah asisten AI yang ramah."}]

# Tampilkan pesan sebelumnya
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Input user
user_input = st.chat_input("Ketik pesan Anda di sini...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        bot_reply = "Maaf, terjadi kesalahan saat menghubungi API."
        st.error(f"Error: {e}")

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
