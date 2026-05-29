import streamlit as st


def render_header():
    """App title and subtitle."""
    st.title("Resume Screener")
    
    st.divider()


def render_inputs() -> tuple:
    """
    Renders the JD text area and file uploader.

    Returns:
        (jd_text, uploaded_file)
    """
    jd = st.text_area(
        "Paste Job Description",
        height=200,
        placeholder="Paste the full job description here...",
    )
    uploaded = st.file_uploader(
        "Upload Resume (PDF or DOCX)",
        type=["pdf", "docx"],
    )
    return jd, uploaded


def render_button(disabled: bool) -> bool:
    """
    Renders the Screen Resume button.

    Returns:
        True if clicked, False otherwise.
    """
    return st.button(
        "Screen Resume",
        disabled=disabled,
        use_container_width=True,
    )


def render_result(result: dict):
    """
    Renders the verdict card.

    Args:
        result: dict with keys verdict, reason, error
    """
    if result["error"]:
        st.error(result["error"])
        return

    verdict = result["verdict"]
    reason  = result["reason"]
    is_fit  = verdict == "Fit"

    color      = "#16a34a" if is_fit else "#dc2626"
    background = "#f0fdf4" if is_fit else "#fef2f2"
    icon       = "✅" if is_fit else "❌"
    label      = "Fit for the Role" if is_fit else "Not Fit for the Role"

    st.markdown(f"""
    <div style="
        border-left: 5px solid {color};
        background: {background};
        padding: 22px 26px;
        border-radius: 10px;
        margin-top: 20px;
    ">
        <h2 style="color:{color}; margin:0 0 10px 0;">{icon} {label}</h2>
        <p style="color:#374151; margin:0; font-size:1rem; line-height:1.7;">{reason}</p>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Small footer."""
    st.divider()
    