import os
import textwrap
import streamlit as st
from transformers.pipelines import pipeline
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

# --------------------------
# 1. Streamlit page config
# --------------------------
st.set_page_config(
    page_title="Course RAG Chatbot",
    page_icon="🎓",
)
st.title("🎓 Course RAG Chatbot")
st.write("Ask questions about courses offered by different institutes. Answers are based only on the text files in the /data folder.")

# --------------------------
# 2. Directory paths
# --------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")
COLLECTION_NAME = "course_rag_collection"

# --------------------------
# 3. Load all text files
# --------------------------
def load_all_text_files(data_dir: str):
    texts = {}
    for fname in os.listdir(data_dir):
        if fname.lower().endswith(".txt"):
            fpath = os.path.join(data_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                texts[fname] = f.read()
    return texts

# --------------------------
# 4. Simple chunking
# --------------------------
def simple_chunk_text(text: str, max_chars: int = 600):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    for para in paragraphs:
        if len(para) <= max_chars:
            chunks.append(para)
        else:
            wrapped = textwrap.wrap(para, width=max_chars)
            chunks.extend(wrapped)
    cleaned = []
    for c in chunks:
        c = c.strip()
        if c and c not in cleaned:
            cleaned.append(c)
    return cleaned

# --------------------------
# 5. ChromaDB collection
# --------------------------
@st.cache_resource
def get_chroma_collection():
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_fn,
    )

    if collection.count() == 0:
        all_files = load_all_text_files(DATA_DIR)
        ids, documents, metadatas = [], [], []
        for filename, text in all_files.items():
            chunks = simple_chunk_text(text)
            for i, chunk in enumerate(chunks):
                ids.append(f"{filename}-chunk-{i}")
                documents.append(chunk)
                metadatas.append({"source": filename})
        collection.add(documents=documents, ids=ids, metadatas=metadatas)
    return collection

# --------------------------
# 6. Load text generation model
# --------------------------
@st.cache_resource
def load_model():
    generator = pipeline(
        "text2text-generation",
        model="google/flan-t5-large",
        max_new_tokens=200
    )
    return generator

# --------------------------
# 7. Retrieve context
# --------------------------
def retrieve_context(query: str, top_k: int = 6):
    collection = get_chroma_collection()
    result = collection.query(query_texts=[query], n_results=top_k)
    docs = result.get("documents", [[]])[0]
    metas = result.get("metadatas", [[]])[0]
    return list(zip(docs, metas))

# --------------------------
# 8. Build prompt
# --------------------------
def build_prompt(history, user_message, used_context):
    parts = []
    parts.append(
        "You are a Course Question-Answering assistant.\n"
        "You MUST answer ONLY using the context below.\n"
        "If the answer is not present in the context, reply exactly:\n"
        "\"I don't know from this text.\"\n\n"
        "Context:\n"
    )
    for i, (ctx, meta) in enumerate(used_context, start=1):
        parts.append(f"[Chunk {i}] (Source: {meta['source']})\n{ctx}\n")
    parts.append("\nConversation:\n")
    for msg in history:
        role = "User" if msg["role"] == "user" else "Bot"
        parts.append(f"{role}: {msg['text']}\n")
    parts.append(f"User: {user_message}\nBot:")
    return "\n".join(parts)

# --------------------------
# 9. Generate answer
# --------------------------
def generate_bot_reply(history, user_message, used_context, generator):
    prompt = build_prompt(history, user_message, used_context)
    output = generator(prompt)
    full = output[0]["generated_text"].strip()
    if full == "":
        return "I don't know from this text."
    return full

# --------------------------
# 10. Session state
# --------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "bot", "text": "Hello! I am a Course RAG Chatbot. Ask me anything about courses from the text files."}
    ]
if "last_used_context" not in st.session_state:
    st.session_state["last_used_context"] = []

# --------------------------
# 11. Sidebar
# --------------------------
st.sidebar.header("⚙️ Settings")
if st.sidebar.button("Clear Chat"):
    st.session_state["messages"] = [{"role": "bot", "text": "Chat cleared. How can I help you?"}]
    st.session_state["last_used_context"] = []
    st.rerun()

# --------------------------
# 12. Display conversation
# --------------------------
st.subheader("💬 Chat")
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"*You:* {msg['text']}")
    else:
        st.markdown(f"*Bot:* {msg['text']}")

# --------------------------
# 13. Input box
# --------------------------
st.subheader("Ask a question")
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your question:")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip() != "":
    q = user_input.strip()
    with st.spinner("Searching knowledge base..."):
        context = retrieve_context(q)
    generator = load_model()
    history = st.session_state["messages"]
    with st.spinner("Generating answer..."):
        reply = generate_bot_reply(history, q, context, generator)
    st.session_state["messages"].append({"role": "user", "text": q})
    st.session_state["messages"].append({"role": "bot", "text": reply})
    st.session_state["last_used_context"] = context
    st.rerun()

# --------------------------
# 14. Show context used
# --------------------------
if st.session_state["last_used_context"]:
    with st.expander("📚 Context used"):
        for i, (ctx, meta) in enumerate(st.session_state["last_used_context"], start=1):
            st.markdown(f"### Chunk {i} — {meta['source']}")
            st.write(ctx)
