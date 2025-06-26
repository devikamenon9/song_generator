import streamlit as st
import random
name = st.text_input("enter your name: ")
st.write("hey there", (name),"welcome to song selection")
# Step 1: Mood-to-songs mapping
mood_quotes = {
    "happy": [
        ("Daylight", "I once believed love would be burning red, but it's golden, like daylight."),
        ("Kiss You", "So tell me, girl, if every time we touch, you get this kinda rush…")
    ],
    "sad": [
        ("I Love You I'm Sorry", "I love you, I'm sorry. I still think about you every day."),
        ("Zaalima", "Jo teri khatir tadpe pehle se hi, kya usse tadpana?")
    ],
    "romantic": [
        ("Mast Magan","sheesh mahal na mujhko sathaye, tere sang sukhi roti khaye" ),
        ("Style", "We never go out of style.")
    ],
    "nostalgic": [
        ("So High School", "I feel so high school every time I look at you."),
        ("Daylight", "I want to be defined by the things that I love.")
    ],
    "sassy": [
        ("You Need to Calm Down", "You need to just stop, like, can you just not step on my gown?")
    ]
}


st.title("🎭 Mood-Based Lyric Generator 🎶")
st.write("How are you feeling today?")
st.write("Options: happy, sad, romantic, nostalgic, sassy")
mood = st.selectbox("How are you feeling?", list(mood_quotes.keys()))

# 🎁 Show quote when button is clicked
if st.button("✨ Give me a lyric!"):
    song, quote = random.choice(mood_quotes[mood])
    st.success(f"🎵 *{song}*")
    st.markdown(f"💬 *\"{quote}\"*")

# 🌈 Optional decoration
st.markdown("---")
st.caption("Built with ❤️ for your heart, by you 🫶")