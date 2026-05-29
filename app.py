from dotenv import load_dotenv
import streamlit as st

from utils.extractor import extract_text
from core.screener  import screen
from ui.components  import (
    render_header,
    render_inputs,
    render_button,
    render_result,
    render_footer,
)

load_dotenv()

# ── Page config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Resume Screener",
    page_icon="🎯",
    layout="centered",
)

# ── Render UI ─────────────────────────────────────────────────
render_header()

jd, uploaded = render_inputs()

clicked = render_button(disabled=not (jd.strip() and uploaded))

# ── On button click ───────────────────────────────────────────
if clicked:
    # 1. Extract text from uploaded file
    resume_text, extract_err = extract_text(uploaded)

    if extract_err:
        st.error(extract_err)
        st.stop()

    # 2. Screen resume against JD
    with st.spinner("Analyzing resume..."):
        result = screen(jd=jd, resume_text=resume_text)

    # 3. Show verdict
    render_result(result)

render_footer()