from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
import os
import random

proxies_env = os.getenv("PROXIES", "")
PROXIES = proxies_env.split(",") if proxies_env else []

def set_random_proxy():
    if PROXIES:
        proxy = random.choice(PROXIES)
        proxy_url = f"http://{proxy}" if not proxy.startswith("http") else proxy
        os.environ["http_proxy"] = proxy_url
        os.environ["https_proxy"] = proxy_url
        print(f"[INFO] Using proxy: {proxy_url}")
    else:
        print("[INFO] No proxy found, using default network")



def create_db_from_youtube_url(video_url: str,api_key:str) -> FAISS:
    os.environ['GOOGLE_API_KEY'] = api_key
    set_random_proxy()
    embeddings = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db

def query_response(db, query,api_key:str ,k: int =4,):
    os.environ['GOOGLE_API_KEY'] = api_key
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = ChatGoogleGenerativeAI(
        model='gemini-2.5-flash',
        temperature=0.6
    )

    prompt = PromptTemplate(
        input_variables=['question','docs'],
        template="""
You are an expert YouTube Transcript Summarizer AI.

Your task is to answer questions based solely on the transcript of the video provided.

Steps to follow:
1. Carefully read the provided transcript in {docs}.
2. Answer the user's question: {question} using only the information present in the transcript.
3. If the transcript does not contain enough information to answer the question, respond exactly with: "I don't know".
4. Your answers should be detailed, clear, and well-structured. Use paragraphs if necessary.
5. Avoid including information not present in the transcript.

Focus on being informative, precise, and factual. Keep the language natural and easy to understand.
""",
    )

    chain = prompt | llm

    response = chain.invoke({'question': query, 'docs': docs_page_content})
    
    if hasattr(response, "content"):
        return response.content
    return str(response)
