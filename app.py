import streamlit as st
from src.summarizer import summarize_text

# design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap');

.stApp {
    background-color: #EBF4DD;
}
            
/* H1 custom */
.custom-h1 {
    font-family: 'Indie Flower', cursive !important;
    font-size: 2rem;
    color: #5A7863;
    text-align: center;
    margin-bottom: 0.5rem;
}

/* H2 custom */
.custom-h2 {
    font-family: 'Indie Flower', cursive !important;
    font-size: 1.5rem;
    color: #5A7863;
    text-align: center;
    margin-bottom: 0.5rem;
}
            
/* Subtitle */
.subtitle {
    font-family: 'Indie Flower', cursive;
    font-size: 1.2rem;
    color: #5A7863;
    text-align: center;
    margin-bottom: 1.5rem;
}
            
/* label */
.ta-label {
    font-family: 'Indie Flower', cursive;
    font-size: 1rem;
    color: #5A7863;
}

/* textarea */
div[data-testid="stTextArea"] textarea {
    font-family: 'Indie Flower', cursive !important;
    font-size: 1rem;
    color: #5A7863;
}
</style>
""", unsafe_allow_html=True)

# title
st.markdown("<h1 class='custom-h1'>News and Article Summarizer!</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Summarize long articles into 3–5 key sentences using T5</div>",
    unsafe_allow_html=True
)

# contents
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("""
    <div class="col1-wrapper">
        <h2 class="custom-h2">Paste Your Article or News Here!</h2>
        <div class="ta-label">Enter text to summarize:</div>
    </div>
    """, unsafe_allow_html=True)

    text = st.text_area(
        label="",
        height=250,
        placeholder="Paste a news article here (200–1000 words works best)..."
    )

    col_a, col_b = st.columns(2)
with col_a:
    st.markdown(
        "<div class='ta-label'>Max Summary Length</div>",
        unsafe_allow_html=True
    )
    max_len = st.slider(
        "",
        min_value=50,
        max_value=150,
        value=60,
        key="max_len"
    )

with col_b:
    st.markdown(
        "<div class='ta-label'>Min Summary Length</div>",
        unsafe_allow_html=True
    )
    min_len = st.slider(
        "",
        min_value=20,
        max_value=50,
        value=30,
        key="min_len"
    )

if st.button("Generate Summary", type="primary", use_container_width=True):
    if text:
        with st.spinner("Generating summary..."):
            summary = summarize_text(text, max_len, min_len)

        st.markdown(
            "<h3 class='summary-title'>Generated Summary</h3>",
            unsafe_allow_html=True
        )
        st.success(summary)


with col2:
    st.markdown("""
    <div class="col2-wrapper">
        <h2 class="custom-h2">Quick Demo</h2>
        <div class="ta-label">Try demo:</div>
    </div>
    """, unsafe_allow_html=True)

    demos = {
        "BBC News Sample": """
        Scientists have discovered a new species of fish in the Pacific Ocean.
        The fish, named Pacificus novus, has unique bioluminescent properties.
        """,
        "Tech News": """
        Apple announced iPhone 16 with revolutionary AI features.
        The new A18 chip enables advanced on-device AI.
        """
    }

    selected = st.selectbox(
        label="",
        options=list(demos.keys()),
        key="demo_select"
    )

    if st.button(
        "Quick Summary",
        key="demo",
        use_container_width=True
    ):
        summary = summarize_text(demos[selected], 60, 20)
        st.success(summary)
