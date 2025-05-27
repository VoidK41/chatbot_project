# 🤖 Chatbot AI Sederhana

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green)

Proyek chatbot berbasis GPT-3.5 ini dirancang untuk membantu bisnis kecil menangani pertanyaan rutin pelanggan, menghemat waktu, dan meningkatkan pelayanan.

## 🚀 Cara Install & Jalankan

1. Clone repository ini:

```bash
git clone https://github.com/VoidK41/chatbot_project
cd chatbot_project
```

2. Install dependensi:

```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:

```bash
streamlit run chatbot_gpt.py
```

## ✨ Fitur Utama
- Respon otomatis berbasis AI (GPT-3.5)
- Antarmuka web sederhana dengan Streamlit
- Bisa di-custom untuk kebutuhan bisnis

## 📸 Screenshot
![Screenshot Chatbot](screenshot.png)


## 📊 Contoh Output

```
User: halo
Bot: Halo! Ada yang bisa saya bantu hari ini?
```

## 👤 Tentang Saya
Saya [KhairuIkramendra], developer AI pemula yang fokus membangun solusi cerdas untuk UMKM.
📩 Kontak: [ikramendra@gmail.com]
LinkedIn: [linkedin.com/in/khairuikramendra](https://www.linkedin.com/in/khairuikramendra)

## 📌 Catatan
- Pastikan API key dari OpenAI sudah disimpan di `st.secrets["OPEN_API_KEY"]`.
- Untuk penggunaan skala lebih besar, pertimbangkan optimasi biaya & batching request.
