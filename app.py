import streamlit as st
from collections import Counter
import string


def decrypt(encrypted_text, key_char):
    if not key_char or len(key_char) != 1:
        return "❌ Key character must be a single character."
    return encrypted_text.replace(key_char, "")


def auto_guess(encrypted_text):
    if not encrypted_text:
        return ''
    # Filter out standard characters
    freqs = Counter(encrypted_text)
    likely_key = ''
    for char, count in freqs.most_common():
        if char not in string.ascii_letters + string.digits + ' ':
            likely_key = char
            break
    return likely_key or freqs.most_common(1)[0][0]


st.set_page_config(page_title="🔐 AI Decryptor", layout="centered")

with st.container():
    st.title("🤖 AI-Powered Visual Decryptor")
    st.markdown(
        "_Decrypt messages by removing unwanted or obfuscating characters. "
        "Let the AI guess or choose your own._"
    )

    encrypted_text = st.text_area("🧬 Encrypted Text", height=150)
    guess_key = auto_guess(encrypted_text)
    st.markdown(
        f"🧠 **AI Guesses Character to Remove:** `{guess_key}`"
    )

    key_char = st.text_input(
        "🔑 Manually Confirm or Override Key Character",
        value=guess_key,
        max_chars=1
    )

    if st.button("💣 Decrypt"):
        result = decrypt(encrypted_text, key_char)
        st.subheader("🧠 Decrypted Output")
        st.markdown(
            f"""
            <div style="
                background-color: #000;
                color: #0f0;
                padding: 15px;
                border: 1px dashed #00ffcc;
                font-family: monospace;
                white-space: pre-wrap;
                word-break: break-word;
                max-height: 300px;
                overflow-y: auto;
                border-radius: 8px;
                margin-top: 10px;
            ">
                {result}
            </div>
            """,
            unsafe_allow_html=True
        )