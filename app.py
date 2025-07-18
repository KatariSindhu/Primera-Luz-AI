import streamlit as st
from newspaper import Article
from langchain_community.llms import Ollama
from googletrans import Translator
import urllib.parse
from gtts import gTTS
import playsound
import os
import uuid


LANGUAGE_MAP = {
    "None": "none",
    "Hindi": "hi", "Bengali": "bn", "Tamil": "ta", "Telugu": "te", "Marathi": "mr",
    "Kannada": "kn", "Gujarati": "gu", "Malayalam": "ml", "Punjabi": "pa", "Urdu": "ur",
    "Spanish": "es", "French": "fr", "German": "de", "Arabic": "ar", "Russian": "ru",
    "Japanese": "ja", "Korean": "ko", "Portuguese": "pt", "Italian": "it", "Chinese (Simplified)": "zh-CN"
}

if "history" not in st.session_state:
    st.session_state.history = []

bg_color = "#FFFFFF"
text_color = "#000000"

st.set_page_config(page_title="Primera Luz AI", page_icon="🌅", layout="centered")

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    input, textarea {{
        background-color: #112233;
        color: {text_color};
        border: 1px solid #444;
    }}
    .stSelectbox, .stRadio {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .stRadio > label, .stSelectbox > label, .stTextInput > label {{
        color: {text_color};
    }}
    .markdown-text-container, .stMarkdown p {{
        color: {text_color} !important;
    }}
    .streamlit-expanderHeader {{
        color: {text_color};
        background-color: #1b2a3a;
    }}
    </style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📄 Summarizer", "ℹ️ About"])

with tab1:
    st.markdown("<h1 style='text-align: center;'>🌅 Primera Luz AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Shining the first light on every story</p>", unsafe_allow_html=True)

    st.markdown("""
        <p style='text-align: center; color: #f1f1f1;'>Currently, Primera Luz AI works best with <strong>English news articles</strong>. Paste a link below to see the summary in seconds.</p>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### 🔗 Enter a news article URL")
    url = st.text_input("Paste the URL below:", placeholder="https://example.com/article")

    summary_style = st.radio("📝 Choose Summary Style", ["Brief Summary", "Bullet Points", "One-liner"], horizontal=True)
    explain_simple = st.checkbox("🧠 Explain Like I'm 5")
    tts_enabled = st.checkbox("🎷 Read Summary Aloud")
    translate_to = st.selectbox("🌐 Translate Summary To", list(LANGUAGE_MAP.keys()))

    summary = ""
    if st.button("🧠 Generate Summary"):
        if not url:
            st.warning("Please enter a valid news article URL.")
        else:
            try:
                with st.spinner("📀 Extracting article..."):
                    article = Article(url)
                    article.download()
                    article.parse()
                    content = article.text

                if not content:
                    st.error("⚠️ Could not extract article content.")
                else:
                    if article.top_image:
                        st.image(article.top_image, caption="🖼 Top Image from the Article", use_container_width=True)

                    word_count = len(content.split())
                    reading_time = round(word_count / 200)
                    st.markdown(f"🕒 Estimated Reading Time: **{reading_time} min** ({word_count} words)")

                    if summary_style == "Brief Summary":
                        prompt = f"Give me a short and concise summary of this article:\n\n{content}"
                    elif summary_style == "Bullet Points":
                        prompt = f"Summarize the article in 5 bullet points:\n\n{content}"
                    else:
                        prompt = f"Give a one-line TL;DR of this article:\n\n{content}"

                    with st.spinner("🧠 Generating summary..."):
                        llm = Ollama(model="tinyllama")
                        summary = llm.invoke(prompt)

                    st.markdown("### 📍 Summary")
                    st.markdown(summary)
                    summary_to_download = summary

                    # Kid Mode- Explain Like I am 5
                    if explain_simple:
                        explain_prompt = f"Explain the following article in extremely simple language for a 5-year-old to understand:\n\n{content}"
                        simple_summary = llm.invoke(explain_prompt)
                        st.markdown("### 👶 Summary (Like You're 5)")
                        st.markdown(simple_summary)
                        summary_to_download = simple_summary
                    else:
                        simple_summary = summary

                    # Translating the summary to some other language
                    if translate_to != "None":
                        lang_code = LANGUAGE_MAP[translate_to]
                        translator = Translator()
                        translated = translator.translate(summary_to_download, dest=lang_code).text
                        st.markdown(f"### 🌍 Translated Summary ({translate_to})")
                        st.markdown(translated)
                        summary_to_download = translated
                    else:
                        lang_code = 'en'

                    # Option to download the summary generated as text file
                    st.download_button(
                        label="📂 Download Summary as .txt",
                        data=summary_to_download,
                        file_name="summary.txt",
                        mime="text/plain"
                    )

                    # Option to share it on Twitter
                    tweet_url = "https://twitter.com/intent/tweet?text=" + urllib.parse.quote(summary[:250])
                    st.markdown(f"[🕊 Tweet this summary]({tweet_url})", unsafe_allow_html=True)

                    # Option to share it on WhatsApp
                    encoded_summary = urllib.parse.quote(summary[:400])
                    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_summary}"
                    st.markdown(f"[📱 Share on WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

                    # TTS(Text To Speech) with gTTS (Streamlit-friendly for cloud)
                    if tts_enabled:
                        try:
                            unique_filename = f"summary_{uuid.uuid4()}.mp3"
                            tts = gTTS(text=summary_to_download, lang=lang_code)
                            tts.save(unique_filename)

                            with open(unique_filename, "rb") as audio_file:
                                audio_bytes = audio_file.read()
                                st.audio(audio_bytes, format="audio/mp3")
                                st.success("🎧 Press play to listen to the summary.")

                            os.remove(unique_filename)  # Cleaning up temporary audio file  

                        except Exception as e:
                             st.error(f"🔇 TTS Error: {e}")

                    st.session_state.history.append(summary)
                    st.session_state.history = st.session_state.history[-5:]

            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("Ensure Ollama is running with: `ollama run tinyllama`")

    if st.session_state.history:
        with st.expander("📜 Summary History (last 5)"):
            for i, s in enumerate(reversed(st.session_state.history), 1):
                st.markdown(f"**{i}.** {s}")

    st.divider()

with tab2:
    st.markdown("## ℹ️ About This App")
    st.markdown("""
**Primera Luz AI** means _First Light_ in Spanish.  
It reflects the clarity this app brings to news — and the creator’s **first step into Generative AI**.

**Purpose:** To help people quickly understand whether a news article deserves their attention.

**Core Features:**
- 💡 Free and fully local GenAI summarizer (no OpenAI API needed)
- ✨ Choose how you want the summary: brief, bullet points, or One-line
- 🌐 Translate summaries to Indian & global languages
- 🖼 Shows article image and reading time
- 📅 ELI5 (Explain Like I'm 5) mode
- 🎷 Text-to-Speech reads it for you (in your chosen language)
- 📂 Download, 🕊 Tweet or 📱 Share on WhatsApp
- 📜 View recent summaries

**Made by:** K Sindhu  
B.Tech-CSE | Coding Enthusiast | AI Explorer | Aspiring Software Developer
    """)

