import os
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="CareLens | AI Healthcare Support",
    page_icon="🩺",
    layout="wide",
)

st.markdown("""
<style>
    .main {background: #f7f9fc;}
    .hero {
        padding: 1.5rem 1.7rem; border-radius: 18px;
        background: linear-gradient(120deg, #123b5d, #176b72);
        color: white; margin-bottom: 1rem;
    }
    .hero h1 {color: white; margin: 0;}
    .hero p {color: #e4f4f5; margin: .4rem 0 0 0;}
    .notice {
        background: #fff7e6; border-left: 5px solid #e0a12b;
        padding:  .9rem 1rem; border-radius: 8px; color: #604514;
    }
    .small-note {color: #64748b; font-size: .88rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🩺 CareLens</h1>
  <p>AI-assisted patient information review and clinical decision support</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="notice">
<b>Educational demonstration only.</b> This app is not a medical device and must
not be used to diagnose, prescribe, triage, or make real patient-care decisions.
Do not enter names, CNIC numbers, phone numbers, addresses, or other identifying
patient information. A qualified healthcare professional must independently
review all findings.
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("About CareLens")
    st.write(
        "CareLens demonstrates how a language model can organise clinical "
        "information, highlight questions for clinician review, and outline "
        "general care-support considerations."
    )
    st.caption("Powered by Groq API + Streamlit")
    st.divider()
    st.subheader("Configuration")
    api_key = st.text_input(
        "Groq API key",
        type="password",
        help="Your key is used for this session only. Do not share it."
    )
    model = st.selectbox(
        "Model",
        ["llama-3.3-70b-versatile", "openai/gpt-oss-20b"],
        index=0,
    )
    st.caption("If a model is unavailable for your Groq account, select another supported model.")

st.subheader("1. Patient information")
left, right = st.columns(2)

with left:
    age = st.number_input("Age", min_value=0, max_value=120, value=35, step=1)
    sex = st.selectbox("Sex (optional clinical context)", ["Not specified", "Female", "Male", "Other / prefer not to say"])
    symptoms = st.text_area(
        "Current symptoms",
        placeholder="Example: persistent cough for 5 days, mild fever, fatigue...",
        height=130,
    )
    duration = st.text_input("Symptom duration", placeholder="Example: 5 days")

with right:
    medical_history = st.text_area(
        "Relevant medical history",
        placeholder="Example: asthma, hypertension, previous surgery, or none known...",
        height=90,
    )
    medications = st.text_area(
        "Current medications and known allergies",
        placeholder="List medicines, doses if known, and allergies. Do not guess.",
        height=90,
    )
    vitals = st.text_area(
        "Available observations / test results",
        placeholder="Example: temperature, pulse, blood pressure, oxygen saturation, lab values...",
        height=90,
    )

st.subheader("2. What should the AI review?")
review_type = st.multiselect(
    "Select review areas",
    [
        "Summarise the information",
        "Highlight possible risk indicators",
        "Suggest questions or tests for clinician consideration",
        "Outline general treatment-support considerations",
        "Identify missing information",
        "Explain benefits and limitations of AI in this case",
    ],
    default=[
        "Summarise the information",
        "Highlight possible risk indicators",
        "Identify missing information",
        "Outline general treatment-support considerations",
    ],
)

st.markdown(
    '<p class="small-note">Use fictional or properly de-identified information for this classroom project.</p>',
    unsafe_allow_html=True,
)

def build_prompt():
    return f"""
You are an educational clinical decision-support assistant. You are NOT a doctor.
Review the de-identified information below for a classroom demonstration.

PATIENT INFORMATION
Age: {age}
Sex: {sex}
Symptoms: {symptoms or "Not provided"}
Duration: {duration or "Not provided"}
Medical history: {medical_history or "Not provided"}
Medications/allergies: {medications or "Not provided"}
Observations/tests: {vitals or "Not provided"}

REQUESTED REVIEW AREAS
{", ".join(review_type) if review_type else "General structured summary"}

STRICT SAFETY RULES:
- Do not claim to diagnose or confirm a disease.
- Do not prescribe medicines, doses, or tell the user to start/stop treatment.
- Do not calculate a definitive risk score.
- Distinguish reported facts from possibilities and unknowns.
- Do not invent missing results or assume normal values.
- Mention that clinical examination and clinician judgement are required.
- If symptoms or observations suggest a possible emergency, clearly advise immediate
  emergency medical assessment. Do not delay this advice with more questions.
- Keep recommendations at the level of general support and questions for a licensed clinician.
- Explain uncertainty and limitations, including bias and incomplete data.

Format the response with these headings:
1. Information summary
2. Findings that may need clinician attention (not a diagnosis)
3. Missing information / questions for the care team
4. Possible next-step considerations for a qualified clinician
5. General patient-support and monitoring considerations
6. AI limitations and safety note

Use clear, cautious language. If the information is insufficient, say so.
"""

if st.button("✨ Analyse patient information", type="primary", use_container_width=True):
    if not symptoms.strip() and not vitals.strip() and not medical_history.strip():
        st.warning("Please enter at least some symptoms, observations, or medical history.")
    elif not api_key.strip():
        st.error("Add your Groq API key in the sidebar first.")
    else:
        try:
            client = Groq(api_key=api_key.strip())
            with st.spinner("Reviewing the information..."):
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You provide cautious, educational healthcare information and never replace a clinician."
                        },
                        {"role": "user", "content": build_prompt()},
                    ],
                    temperature=0.2,
                    max_tokens=1800,
                )
                result = response.choices[0].message.content

            st.divider()
            st.subheader("3. AI-assisted review")
            st.markdown(result)
            st.download_button(
                "Download review as text",
                data=result,
                file_name="carelens_patient_review.txt",
                mime="text/plain",
            )
            st.info(
                "This output is an AI-generated educational summary, not a diagnosis "
                "or treatment plan. A licensed clinician must verify every finding."
            )
        except Exception as e:
            st.error(f"Could not generate the review: {e}")
            st.caption("Check your API key, internet connection, model availability, and Groq account limits.")

st.divider()
st.subheader("How this app demonstrates the task")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**📋 Patient analysis**")
    st.write("Organises symptoms, history, medicines, observations and test results.")
with c2:
    st.markdown("**⚠️ Risk awareness**")
    st.write("Highlights information that may deserve further clinical attention.")
with c3:
    st.markdown("**🧭 Care support**")
    st.write("Suggests clinician questions, missing information and general monitoring considerations.")

st.caption("CareLens is a student project prototype. It has not been clinically validated.")
