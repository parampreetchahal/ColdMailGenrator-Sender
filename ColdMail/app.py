import streamlit as st
import smtplib
import fitz  # PyMuPDF
import requests
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# ------------------ Helper Functions ------------------

def extract_text_from_pdf(uploaded_file):
    if uploaded_file is None:
        return ""
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def generate_cold_email(resume_text, job_description, api_key):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": "You're a helpful assistant skilled in writing professional cold emails."},
        {"role": "user", "content": f"Based on the following resume:\n{resume_text}\n\nAnd this job description:\n{job_description}\n\nWrite a personalized cold email. Make sure it clear and concise don't add any other line expect mail content"}
    ]
    payload = {
        "model": "llama3-70b-8192",
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def send_email_with_attachment(sender_email, receiver_email, password, subject, body, uploaded_file):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if uploaded_file:
        uploaded_file.seek(0)
        attach = MIMEApplication(uploaded_file.read(), _subtype="pdf")
        attach.add_header('Content-Disposition', 'attachment', filename=uploaded_file.name)
        msg.attach(attach)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# ------------------ Streamlit UI ------------------

st.title("📧 Cold Mail Generator & Sender")

st.subheader("Step 1: Upload Resume")
resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

st.subheader("Step 2: Paste Job Description")
job_description = st.text_area("Paste Job Description here")

st.subheader("Step 3: Generate/Edit Cold Mail")

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

if st.button("✨ Generate Email with AI"):
    if not resume_file or not job_description:
        st.error("Please upload resume and enter job description.")
    else:
        resume_text = extract_text_from_pdf(resume_file)
        try:
            cold_mail = generate_cold_email(resume_text, job_description, GROQ_API_KEY)
            st.session_state.generated_mail = cold_mail
        except Exception as e:
            st.error(f"AI generation failed: {e}")

cold_mail = st.text_area(
    "Edit the email before sending:",
    value=st.session_state.get("generated_mail", "Dear Recruiter,\n\nI am excited to apply for..."),
    height=250
)

st.subheader("Step 4: Email Details")
sender_email = st.text_input("Your Gmail Address")
app_password = st.text_input("Your App Password (Google App Password)", type="password")
receiver_email = st.text_input("Recruiter's Email Address")
subject = st.text_input("Email Subject", value="Application for [Job Title]")

if st.button("📨 Send Email"):
    if not (resume_file and job_description and cold_mail and sender_email and app_password and receiver_email):
        st.error("⚠️ Please fill in all fields and upload the resume.")
    else:
        try:
            send_email_with_attachment(sender_email, receiver_email, app_password, subject, cold_mail, resume_file)
            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
