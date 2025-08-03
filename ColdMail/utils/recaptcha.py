import streamlit as st
import streamlit.components.v1 as components
import requests

def display_recaptcha():
    site_key = st.secrets["recaptcha"]["site_key"]
    components.html(f"""
        <script src="https://www.google.com/recaptcha/api.js" async defer></script>
        <form action="?" method="POST">
            <div class="g-recaptcha" data-sitekey="{site_key}"></div>
            <input type="submit" value="Submit">
        </form>
    """, height=120)

def verify_recaptcha(response_token):
    secret_key = st.secrets["recaptcha"]["secret_key"]
    url = "https://www.google.com/recaptcha/api/siteverify"
    payload = {"secret": secret_key, "response": response_token}
    r = requests.post(url, data=payload)
    return r.json().get("success", False)
