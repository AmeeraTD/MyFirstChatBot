
# 🤖 AI Chatbot (Flask + JS + OpenRouter)

A smart, responsive chatbot built using **Python Flask**, **vanilla JavaScript**, and **OpenRouter.ai** for free GPT-style AI conversations. Features a sleek animated gradient background, WhatsApp-style chat bubbles, keyboard and click-based message sending, and secure API integration using `.env`.

> 💡 Developed by **Ameera Thiwanka**  
> 🚫 This project is intellectual property. Do not copy or reuse without permission.

---

## 🎯 Features

- 🔥 ChatGPT-style AI replies (via OpenRouter API)
- ⚡ Animated gradient background
- 💬 WhatsApp-style message layout (user vs bot)
- ⌨️ Press `Enter` or click Send
- 📦 Clean and modular structure (Flask + JS + CSS)
- 🔐 Uses `.env` to secure API keys

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/MyFirstChatBot.git
cd MyFirstChatBot
```

---

### 2. Install Dependencies

```bash
pip install flask requests python-dotenv
```

---

### 3. Create a `.env` File

Create a `.env` file in your root directory with your OpenRouter API key:

```env
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> 🔒 **Never share this key** or push your `.env` file to GitHub!

---

### 4. Add `.env` to `.gitignore`

```gitignore
.env
__pycache__/
*.pyc
venv/
```

---

### 5. Run the App

```bash
python app.py
```

Open in browser:  
[http://localhost:5000](http://localhost:5000)

---

## 🗂️ Project Structure

```bash
MyFirstChatBot/
├── app.py              # Flask backend
├── .env                # Secret API key (not tracked)
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html      # Chat UI
│
└── static/
    ├── style.css       # Gradient background + chat styles
    └── script.js       # Handles sending messages + keyboard support
```

---

## 🧠 Example Messages to Try

- "Tell me a joke"  
- "What is Flask?"  
- "What’s the capital of Japan?"  
- "Give me 3 fun Python project ideas"

---

## 📌 Model in Use

Currently using:

```bash
model: mistralai/mistral-7b-instruct
```

You can change this in `app.py` to try different OpenRouter models.

---

## 👤 About the Developer

I'm **Ameera Thiwanka**, a Computer Science & Engineering undergrad passionate about backend development.

🔗 [LinkedIn](https://linkedin.com/in/ameerathiwanka)  

---

## 🛡 License & Use

This project is created for educational and portfolio purposes.  
It is not licensed for commercial reuse.  
Please contact me before using any part of this code.

---
