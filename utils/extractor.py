import io


def extract_text(file) -> tuple[str, str]:
    """
    Extracts plain text from a PDF or DOCX file object.

    Args:
        file: Streamlit UploadedFile object

    Returns:
        (text, error_message)
        - On success : (extracted_text, "")
        - On failure : ("", error_message)
    """
    ext = file.name.rsplit(".", 1)[-1].lower()
    raw = file.read()

    # ── PDF ──────────────────────────────────────────────────────
    if ext == "pdf":
        try:
            from pypdf import PdfReader
        except ImportError:
            return "", "pypdf not installed. Run: pip install pypdf"

        try:
            reader = PdfReader(io.BytesIO(raw))
            text   = "\n".join(p.extract_text() or "" for p in reader.pages).strip()
        except Exception as e:
            return "", f"Could not read PDF: {str(e)}"

    # ── DOCX ─────────────────────────────────────────────────────
    elif ext in ("docx", "doc"):
        try:
            from docx import Document
        except ImportError:
            return "", "python-docx not installed. Run: pip install python-docx"

        try:
            doc  = Document(io.BytesIO(raw))
            text = "\n".join(p.text for p in doc.paragraphs).strip()
        except Exception as e:
            return "", f"Could not read DOCX: {str(e)}"

    else:
        return "", f"Unsupported file type '.{ext}'. Upload PDF or DOCX."

    # ── Validation ───────────────────────────────────────────────
    if not text:
        return "", "No text found in file. It may be image-based or corrupted."

    return text[:2500], ""   # truncate to stay within LLM token limits