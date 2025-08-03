
# 🚀 Streamlit App with reCAPTCHA and GROQ Integration

This is a Streamlit-based web application that uses Google reCAPTCHA for user verification and GROQ API for intelligent responses. It ensures that only human users can interact with the app, making it more secure and interactive.

---

## 🌐 Features

- ✅ Google reCAPTCHA v2 verification
- 🤖 Integration with GROQ API for AI-driven text responses
- 🧠 Fast and lightweight interface powered by Streamlit
- 🔐 Secret key management using Streamlit Secrets Manager
- 🆓 Free deployment using Streamlit Community Cloud

---

## 📁 Project Structure



├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── secrets.toml       # Store API keys and credentials (used on Streamlit Cloud)





## 🔧 Setup Instructions (Local)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.streamlit/secrets.toml`:**

   ```toml
   [recaptcha]
   site_key = "your_recaptcha_site_key"
   secret_key = "your_recaptcha_secret_key"

   GROQ_API_KEY = "your_groq_api_key"
   ```

5. **Run the app locally:**

   ```bash
   streamlit run app.py
   ```

---





## 🛠 Built With

* [Streamlit](https://streamlit.io/)
* [Google reCAPTCHA v2](https://www.google.com/recaptcha/)
* [GROQ API](https://groq.com/)
* Python 3.9+

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

* Thanks to Streamlit for the free hosting!
* Special thanks to OpenAI for their API inspiration.


