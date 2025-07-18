## 🌅 Primera Luz AI 
**Shining the first light on every story.**

As someone who values simplicity and discipline, I wanted my first GenAI project to cut through the noise and get to the point. I built this app to help people quickly understand if a piece of content is worth their attention.

## 🚀 Features

- 📰 **Summarize any news article** instantly by just pasting the URL
- ✂️ Choose your summary style: **Brief**, **Bullet Points**, or **One-liner**
- 👶 "Explain Like I'm 5" mode for ultra-simple summaries
- 🌍 Translate summary into **20+ global & Indian languages**
- 📸 Auto-fetches **top image** and shows **estimated reading time**
- 🎧 **Text-to-Speech** for summaries in your selected language
- 📂 Download summaries as `.txt`
- 📱 **Share to WhatsApp** or 🕊 **Tweet** directly
- 🕒 View your **recent summary history**

## 🧑‍💻 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Model**: [TinyLLaMA](https://ollama.com/library/tinyllama) via [Ollama](https://ollama.com/)
- **NLP Tools**: `newspaper3k`, `googletrans`, `gTTS`
- **AI Framework**: LangChain (community)

## Goal
“The goal is to make news easier for everyone — no matter their age, language or attention span.”

## Screenshots

![WhatsApp Image 2025-07-18 at 21 34 23_4c8e4399](https://github.com/user-attachments/assets/270117ef-b6ea-421c-a106-7c3c8852834e)
![WhatsApp Image 2025-07-18 at 21 35 15_4584dd20](https://github.com/user-attachments/assets/d4c634fd-4d53-4dac-a4ec-37ccd1a9c9af)
![WhatsApp Image 2025-07-18 at 21 35 43_6e7b0cf4](https://github.com/user-attachments/assets/7977c1b7-6095-40eb-9a5c-6016457bedfc)
![WhatsApp Image 2025-07-18 at 21 36 16_febdf1ff](https://github.com/user-attachments/assets/2f15e754-4b0f-45b9-8455-768011021c9a)
![WhatsApp Image 2025-07-18 at 21 40 25_eae8cfb0](https://github.com/user-attachments/assets/0236d13b-dff0-42a9-a581-0fd3930012a0)

## 📦 Setup Instructions  

### 1️⃣ Clone the Repository  
`git clone https://github.com/yourusername/primera-luz-ai.git`  
`cd primera-luz-ai`  

### 2️⃣ Create Virtual Environment  
**For Windows:**  
`python -m venv venv`   
`venv\Scripts\activate` 

**For macOS/Linux:**  
`python3 -m venv venv`    
`source venv/bin/activate`  

### 3️⃣ Install Requirements
`pip install -r requirements.txt`

### 4️⃣ Install and Run Ollama (for TinyLLaMA)
⚙️ Ollama is used to run the TinyLLaMA model locally.

➤ **Download & Install Ollama:**  
Visit: https://ollama.com/download  
➤ **Pull the TinyLLaMA model:**  
`ollama pull tinyllama`  
➤ **Start the Ollama server (if not already running):**  
`ollama run tinyllama`   
**Note:** Make sure this terminal remains running while using the app.  

### 5️⃣ Run the App  
streamlit run app.py  

---

## 🚀 What's Next?

We're excited to share that **Version 2.0** of *Primera Luz AI* is in the works!

🔧 Planned Enhancements:
- 🌐 Fully deployable **online version**
- 💬 Smoother and faster LLM integration
- 🎨 Improved UI and UX
- 🧠 More intelligent response handling
- 📲 Mobile-responsive interface

Stay tuned for a better, faster, and more accessible experience in the upcoming release!

> 💡 Follow this repository or ⭐ star it to get notified when **v2.0** launches!

## ✨ Let's Connect

For feedback, feature requests or collaborations:  
Feel free to connect on [LinkedIn](www.linkedin.com/in/k-sindhu-1560a9253) or follow me on [GitHub](https://github.com/KatariSindhu).  

