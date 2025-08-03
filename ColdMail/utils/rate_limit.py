import streamlit as st
from datetime import datetime, timedelta

MAX_ATTEMPTS = 3
TIME_WINDOW = timedelta(minutes=10)


def is_limited():
    now = datetime.now()
    attempts = st.session_state.get("attempts", [])
    attempts = [t for t in attempts if now - t < TIME_WINDOW]

    if len(attempts) >= MAX_ATTEMPTS:
        return True

    attempts.append(now)
    st.session_state["attempts"] = attempts
    return False
