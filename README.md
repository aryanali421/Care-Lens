# CareLens — AI Healthcare Support Demo

A beginner-friendly Streamlit demonstration using the Groq API. It organises de-identified patient information and generates a cautious educational review.

## Important safety note
This is a classroom prototype, not a medical device. It must not be used for diagnosis, prescribing, triage, or real patient-care decisions. Use fictional or properly de-identified data only. A licensed healthcare professional must independently review all output.

## 1. Requirements
- Python 3.10 or newer
- Internet connection
- Groq API key

## 2. Install
Open a terminal in this folder and run:

```bash
python -m pip install -r requirements.txt
```

## 3. Run
```bash
streamlit run app.py
```

Streamlit will open the app in your browser. Paste your Groq API key into the sidebar, enter fictional/de-identified information, select the review areas, and click **Analyse patient information**.

## 4. Get a Groq API key
Create or access your Groq account and generate an API key in the Groq developer console. Keep the key private. Do not upload it to GitHub or share it in screenshots.

## 5. Deploy on Streamlit Community Cloud
1. Create a GitHub repository.
2. Upload `app.py` and `requirements.txt`.
3. Create a Streamlit Community Cloud app and select the repository and `app.py`.
4. Add your Groq key using Streamlit secrets or enter it in the app sidebar.

For a public deployment, prefer Streamlit secrets rather than asking visitors to paste a key that belongs to you. Never commit API keys to GitHub.

## Features
- Patient information form
- Symptoms, medical history, medications/allergies and observations
- Selectable AI review sections
- Groq-powered response
- Downloadable text report
- Clinical safety and privacy warnings
