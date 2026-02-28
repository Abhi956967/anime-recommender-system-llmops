import sys
import os

# ---------- FIX PYTHON PATH ----------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# ---------- IMPORTS ----------
import streamlit as st
from pipeline.pipeline_build import AnimeRecommendationPipeline
from dotenv import load_dotenv
import time

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Anime AI Recommender",
    page_icon="🎌",
    layout="wide",
)

load_dotenv()

# ---------- CUSTOM CSS (PORTFOLIO UI) ----------
st.markdown("""
<style>

body {
    background-color: #0e1117;
}

.main-title {
    font-size:45px;
    font-weight:700;
    text-align:center;
    color:white;
}

.subtitle {
    text-align:center;
    color:#bdbdbd;
    font-size:18px;
    margin-bottom:30px;
}

.card {
    background: rgba(255,255,255,0.05);
    padding:20px;
    border-radius:15px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
    margin-bottom:15px;
}

.stTextInput>div>div>input {
    background-color:#1c1f26;
    color:white;
    border-radius:10px;
}

.sidebar .sidebar-content {
    background-color:#111318;
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD PIPELINE ----------
@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

# ---------- SIDEBAR ----------
st.sidebar.title("🎌 Anime AI")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🤖 Recommender", "📊 About Model", "👨‍💻 About Project"]
)

st.sidebar.markdown("---")
st.sidebar.info(
"""
**LLMOps Project**

Built using:
- LLM + Embeddings
- Vector Search
- Streamlit
- End-to-End Pipeline
"""
)

# =====================================================
# HOME PAGE
# =====================================================
if page == "🏠 Home":

    st.markdown('<p class="main-title">Anime Recommender AI 🎌</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Discover anime using Natural Language — powered by LLMOps</p>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        🎯 <b>Smart Recommendations</b><br>
        Describe your mood and get AI-curated anime.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        ⚡ <b>LLM Powered</b><br>
        Uses embeddings + semantic search pipeline.
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        🚀 <b>Production Ready</b><br>
        Built using modern LLMOps architecture.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔥 Try Example Prompts")

    st.code("""
• emotional anime like your lie in april
• dark psychological anime
• funny school anime
• action anime with strong female lead
""")

# =====================================================
# RECOMMENDER PAGE
# =====================================================
elif page == "🤖 Recommender":

    st.markdown("## 🎌 Anime Recommendation Engine")

    query = st.text_input(
        "Describe what anime you want:",
        placeholder="Example: light hearted anime with school settings"
    )

    if "history" not in st.session_state:
        st.session_state.history = []

    if query:
        with st.spinner("🤖 AI is finding perfect anime for you..."):
            time.sleep(1)
            response = pipeline.recommend(query)

        st.success("Recommendations Ready!")

        st.markdown("### ⭐ Recommended Anime")

        # Display result card
        st.markdown(
            f"""
            <div class="card">
            {response}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Save history
        st.session_state.history.append((query, response))

    # -------- HISTORY --------
    if st.session_state.history:
        st.markdown("### 🕘 Previous Searches")

        for q, r in reversed(st.session_state.history[-5:]):
            with st.expander(q):
                st.write(r)

# =====================================================
# MODEL PAGE
# =====================================================
elif page == "📊 About Model":

    st.markdown("## 🤖 Model Architecture")

    st.markdown("""
    ### LLMOps Pipeline

    1. User Query Input  
    2. Text Embedding Generation  
    3. Vector Database Search  
    4. Similarity Matching  
    5. LLM Response Generation  
    6. Recommendation Output
    """)

    st.info("This demonstrates an End-to-End LLMOps workflow suitable for production AI systems.")

# =====================================================
# PROJECT PAGE
# =====================================================
elif page == "👨‍💻 About Project":

    st.markdown("## 🚀 Anime Recommender System")

    st.markdown("""
This project demonstrates a **complete LLMOps lifecycle**:

✅ Data Processing Pipeline  
✅ Embedding Generation  
✅ Vector Search Retrieval  
✅ LLM-based Recommendation  
✅ Streamlit Deployment  

### Tech Stack
- Python
- LLM APIs
- Vector Database
- Streamlit
- Docker (optional)
- CI/CD Ready
""")

    st.success("Portfolio-ready AI application.")