# 🤖 AI Chatbot (Flask + JS + OpenRouter)

A smart, responsive chatbot built using **Python Flask**, **vanilla JavaScript**, and **OpenRouter.ai** for free GPT-style AI conversations. Features a sleek animated gradient background, WhatsApp-style chat bubbles, and secure API integration using `.env`.

> 💡 Developed by **Ameera Thiwanka**  
> 🚫 This project is intellectual property. Do not copy or reuse without permission.

---

## 🎯 Features

- 🔥 ChatGPT-style AI replies (via OpenRouter API)
- ⚡ Responsive UI with animated gradient background
- 💬 WhatsApp-style chat bubbles (user on right, bot on left)
- ⌨️ Supports Enter key and button click
- 🧠 Message history (in session)
- 🔐 API key hidden using `.env`
- ✅ Clean and modular codebase

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/MyFirstChatBot.git
cd MyFirstChatBot

### 2. Install Dependencies

```bash
pip install flask requests python-dotenv

### 3. Create a `.env` File

Create a `.env` file in your root directory with your OpenRouter API key:

```env
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

### 4. Add `.env` to `.gitignore`

```gitignore
.env
__pycache__/
*.pyc
venv/

### 5. Run the App

```bash
python app.py
Open in browser:
http://localhost:5000

## 🗂️ Project Structure
---

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

