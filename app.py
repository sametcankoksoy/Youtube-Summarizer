import streamlit as st
import main as lch

st.set_page_config(
    page_title="YouTube Transcript Summarizer",
    page_icon="📝",
    layout="wide"
)

with st.sidebar:
        st.title('⚙️ Settings')
        api_key = st.text_input(
            label='🔑 API Key',
            type='default',
            placeholder='Enter Gemini API Key',
        )
        query= st.text_input(
                '❓ Question',
                placeholder='Ask me about the video',
                key='Question'
        )
        "👉 [Get an Gemini API Key](https://aistudio.google.com/app/apikey)"

st.title("🎥 YouTube Video Summarizer")
st.subheader("Enter a YouTube link and AI will summarize it for you.")
youtube_url = st.text_input("YouTube Video URL", placeholder="")

if st.button("📝 Get Summary") and youtube_url and query and api_key:
    with st.spinner("Preparing the video summary..."):
        db = lch.create_db_from_youtube_url(youtube_url,api_key)
        response = lch.query_response(db, query,api_key)

    st.subheader("Answer")
    st.markdown(response)


