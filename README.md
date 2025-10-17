## Overview

With this application, our goal is to automatically fetch long YouTube video transcripts, generate meaningful and quick summaries, and provide question-answering based on the content, helping users save time. This way, you can access summaries or specific information without having to watch the whole video.

### What Does It Make Easier?
- Reading and summarizing the content of YouTube videos.
- Quickly understanding what a video is about without watching it in full.
- Getting direct answers to specific questions based on the video transcript.
- Practical summarization for academic, educational, research, or general knowledge purposes from long videos.

### What Did We Use?
- **Python** language and Streamlit for a user-friendly web interface.
- **youtube-transcript-api** to automatically fetch video transcripts.
- **LangChain** framework for text processing, vector database creation, and LLM integration.
- **Google Gemini (Generative AI) API** for text embeddings and natural language processing.
- **FAISS** for fast and efficient vector-based search.
- **Proxy support** to overcome YouTube API access issues.

By leveraging modern AI services for the technical infrastructure, we aim to deliver maximum information with minimum user input.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/sametcankoksoy/Youtube-Summarizer.git
    cd Youtube-Summarizer
    ```

2. **Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```
    Make sure you have the following packages (they should be in `requirements.txt`):
    - `streamlit`
    - `langchain`
    - `langchain-google-genai`
    - `langchain-community`
    - `youtube-transcript-api`
    - `faiss-cpu` (or `faiss-gpu`)

3. **(Optional) Set Proxy List**

   If you need to use a proxy to fetch YouTube transcripts, create a `.env` file:
   ```
   PROXIES=http://proxy1.com:8080,http://proxy2.com:8080
   ```

4. **Get your Google Gemini API Key:**  
   [Create an API key from Google AI Studio](https://aistudio.google.com/app/apikey)

## Usage

1. **Start the application:**
    ```bash
    streamlit run app.py
    ```

2. **On the web interface:**
    - Enter your Gemini API key.
    - Enter your question (e.g., "What is this video about?" or "List the main topics.").
    - Enter the YouTube video URL.
    - Click "Get Summary".
    - Get your answer and summary based only on the transcript of the video.

---
