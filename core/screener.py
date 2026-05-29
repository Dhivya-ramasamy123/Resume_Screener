from core.llm import get_llm


# ── Prompt ────────────────────────────────────────────────────
PROMPT_TEMPLATE = """You are an experienced recruiter. Read the job description and the
candidate's resume carefully, then decide if the candidate is a good fit.

Respond in EXACTLY this format (no extra text):
VERDICT: Fit   OR   VERDICT: Not Fit
include the response with role like fit for the ML role
REASON: <2-3 sentences explaining your decision>

Job Description:
{jd}

Resume:
{resume}"""


def screen(jd: str, resume_text: str) -> dict:
    """
    Runs the screening and returns a result dict.

    Args:
        jd          : job description string
        resume_text : extracted resume text

    Returns:
        {
            "verdict" : "Fit" | "Not Fit" | "Unknown",
            "reason"  : str,
            "error"   : str   (empty string if no error)
        }
    """
    # ── Get LLM ──────────────────────────────────────────────────
    llm, err = get_llm()
    if err:
        return {"verdict": "Unknown", "reason": "", "error": err}

    # ── Build prompt ──────────────────────────────────────────────
    prompt = PROMPT_TEMPLATE.format(
        jd=jd[:2000],
        resume=resume_text[:2500],
    )

    # ── Call LLM ─────────────────────────────────────────────────
    try:
        response = llm.invoke(prompt)
        output   = response.content.strip()
    except Exception as e:
        return {"verdict": "Unknown", "reason": "", "error": f"LLM error: {str(e)}"}

    # ── Parse response ────────────────────────────────────────────
    return _parse(output)


def _parse(output: str) -> dict:
    """
    Parses the LLM response string into verdict + reason.
    Gracefully handles unexpected formats.
    """
    verdict = "Unknown"
    reason  = output   # fallback: show raw output

    for line in output.splitlines():
        line_up = line.upper()

        if line_up.startswith("VERDICT:"):
            value = line.split(":", 1)[-1].strip().lower()
            verdict = "Not Fit" if "not" in value else "Fit"

        elif line_up.startswith("REASON:"):
            reason = line.split(":", 1)[-1].strip()

    return {"verdict": verdict, "reason": reason, "error": ""}