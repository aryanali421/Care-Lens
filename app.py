
import streamlit as st
from groq import Groq
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="CareLens | Clinical Intelligence",
    page_icon="✚",
    layout="wide",
    initial_sidebar_state="expanded"
)

MODEL = "openai/gpt-oss-120b"

# --------------------------------------------------
# DARK MEDICAL THEME
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #080F1C;
    color: #E8F0F7;
}

.main .block-container {
    max-width: 1250px;
    padding: 2rem 3rem;
}

[data-testid="stSidebar"] {
    background: #0D1726;
    border-right: 1px solid #1D3045;
}

h1, h2, h3 {
    color: #F1F7FC !important;
    font-weight: 700 !important;
}

p, label, .stMarkdown {
    color: #C2D0DE;
}

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #111D2E !important;
    color: #F1F7FC !important;
    border: 1px solid #263B52 !important;
    border-radius: 10px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border: 1px solid #35D6C5 !important;
    box-shadow: 0 0 0 1px #35D6C5 !important;
}

.stButton button,
.stDownloadButton button {
    background: #20BBAA;
    color: #06131D !important;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1.2rem;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton button:hover,
.stDownloadButton button:hover {
    background: #35D6C5;
    transform: translateY(-2px);
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #111D2E;
    border: 1px solid #22364D;
    border-radius: 14px;
}

[data-testid="stExpander"] {
    background: #111D2E;
    border: 1px solid #22364D;
    border-radius: 12px;
}

[data-testid="stMetric"] {
    background: #111D2E;
    padding: 18px;
    border: 1px solid #22364D;
    border-radius: 12px;
}

hr {
    border-color: #263B52;
}

#MainMenu, footer {
    visibility: hidden;
}

.stProgress > div > div {
    background-color: #35D6C5;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# API CONFIGURATION
# --------------------------------------------------

try:
    api_key = st.secrets.get("GROQ_API_KEY", "")
except Exception:
    api_key = ""

if not api_key:
    st.error(
        "Groq API key is missing. Add GROQ_API_KEY "
        "to your Streamlit Secrets."
    )
    st.stop()

client = Groq(api_key=api_key)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "patient_name" not in st.session_state:
    st.session_state.patient_name = ""


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("""
    <div style="padding: 15px 0 25px 0;">
        <div style="font-size: 34px; color: #35D6C5;">
            ✚
        </div>
        <h2 style="margin:0; color:white;">CareLens</h2>
        <p style="font-size:12px; color:#8DA3B8;">
            CLINICAL INTELLIGENCE PLATFORM
        </p>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "NAVIGATION",
        ["Patient Analysis", "About CareLens"],
        label_visibility="visible"
    )

    st.divider()

    st.markdown("### System Status")
    st.success("Interface Online")
    st.success("Groq API Configured")

    st.caption(f"Model: {MODEL}")

    st.divider()

    st.caption("CareLens v1.0")
    st.caption("AI-assisted clinical decision support")


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div style="margin-bottom: 25px;">
    <p style="color:#35D6C5; font-size:13px;
    letter-spacing:2px; font-weight:700;">
        CLINICAL INTELLIGENCE
    </p>
    <h1 style="font-size:38px; margin-bottom:5px;">
        CareLens Dashboard
    </h1>
    <p style="color:#8DA3B8;">
        Patient assessment and AI-assisted clinical insights.
    </p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PATIENT ANALYSIS PAGE
# --------------------------------------------------

if page == "Patient Analysis":

    st.markdown("## Patient Information")
    st.caption("Enter the available patient information below.")

    with st.form("patient_form"):

        st.markdown("### 01 · Basic Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            patient_name = st.text_input(
                "Patient Name",
                placeholder="Enter patient name"
            )

        with col2:
            age = st.number_input(
                "Age",
                min_value=0,
                max_value=120,
                value=25
            )

        with col3:
            sex = st.selectbox(
                "Sex",
                ["Not specified", "Male", "Female", "Other"]
            )

        st.divider()

        st.markdown("### 02 · Symptoms")

        symptoms = st.text_area(
            "Describe the symptoms",
            placeholder="Describe the patient's symptoms...",
            height=130
        )

        col1, col2 = st.columns(2)

        with col1:
            duration = st.text_input(
                "Symptom Duration",
                placeholder="e.g. 3 days"
            )

        with col2:
            severity = st.select_slider(
                "Symptom Severity",
                options=["Mild", "Moderate", "Severe", "Very Severe"]
            )

        st.divider()

        st.markdown("### 03 · Medical Background")

        medical_history = st.text_area(
            "Medical History",
            placeholder="Previous conditions, surgeries, family history..."
        )

        medications = st.text_area(
            "Current Medications",
            placeholder="List current medications..."
        )

        allergies = st.text_input(
            "Known Allergies",
            placeholder="Enter known allergies or write None"
        )

        st.divider()

        st.markdown("### 04 · Clinical Measurements")

        col1, col2, col3 = st.columns(3)

        with col1:
            temperature = st.text_input(
                "Temperature",
                placeholder="e.g. 37.2 °C"
            )

        with col2:
            blood_pressure = st.text_input(
                "Blood Pressure",
                placeholder="e.g. 120/80 mmHg"
            )

        with col3:
            heart_rate = st.text_input(
                "Heart Rate",
                placeholder="e.g. 75 bpm"
            )

        oxygen = st.text_input(
            "Oxygen Saturation (SpO₂)",
            placeholder="e.g. 98%"
        )

        test_results = st.text_area(
            "Laboratory / Imaging Results",
            placeholder="Enter available test results..."
        )

        st.divider()

        st.markdown("### 05 · Analysis Requirements")

        analysis_areas = st.multiselect(
            "Select areas to explore",
            [
                "Possible conditions",
                "Differential considerations",
                "Relevant investigations",
                "Treatment considerations",
                "Lifestyle and prevention",
                "Warning signs and urgency"
            ],
            default=[
                "Possible conditions",
                "Differential considerations",
                "Relevant investigations",
                "Warning signs and urgency"
            ]
        )

        submitted = st.form_submit_button(
            "✦ Generate Clinical Analysis",
            use_container_width=True
        )

    # --------------------------------------------------
    # GENERATE ANALYSIS
    # --------------------------------------------------

    if submitted:

        if not symptoms.strip():
            st.warning("Please enter the patient's symptoms.")

        elif not analysis_areas:
            st.warning("Please select at least one analysis area.")

        else:

            patient_data = f"""
PATIENT INFORMATION

Name: {patient_name or "Not provided"}
Age: {age}
Sex: {sex}

SYMPTOMS

Symptoms: {symptoms}
Duration: {duration or "Not provided"}
Severity: {severity}

MEDICAL BACKGROUND

Medical History: {medical_history or "Not provided"}
Medications: {medications or "Not provided"}
Allergies: {allergies or "Not provided"}

CLINICAL MEASUREMENTS

Temperature: {temperature or "Not provided"}
Blood Pressure: {blood_pressure or "Not provided"}
Heart Rate: {heart_rate or "Not provided"}
Oxygen Saturation: {oxygen or "Not provided"}

TEST RESULTS

{test_results or "No test results provided"}

REQUESTED ANALYSIS

{", ".join(analysis_areas)}
"""

            system_prompt = """
You are CareLens, an AI clinical information assistant.

Your role is to help organize patient information and provide
educational, evidence-informed clinical considerations.

IMPORTANT RULES:

1. Never claim to provide a confirmed diagnosis.
2. Clearly distinguish possibilities from established facts.
3. Do not invent patient information, examination findings,
   laboratory values, or test results.
4. Explain uncertainty and missing information.
5. Do not prescribe medication or invent dosages.
6. Identify emergency warning signs prominently.
7. Recommend professional medical evaluation where appropriate.
8. If symptoms suggest an emergency, prioritize urgent care
   instructions over routine analysis.

STRUCTURE YOUR RESPONSE:

# Clinical Overview
Summarize the provided information.

# Possible Conditions
Discuss relevant possibilities and explain why they may fit.
Do not present them as confirmed diagnoses.

# Differential Considerations
Explain other possibilities and what would help distinguish them.

# Recommended Investigations
Suggest relevant assessments or tests for a clinician to consider.

# Treatment Considerations
Provide general educational information, not prescriptions.

# Warning Signs and Urgency
Explain when immediate medical attention is needed.

# Missing Information
Identify important information that would improve assessment.

Use clear professional language, headings, and bullet points.
"""

            try:

                with st.spinner(
                    "CareLens is analyzing the patient information..."
                ):

                    response = client.chat.completions.create(
                        model=MODEL,
                        messages=[
                            {
                                "role": "system",
                                "content": system_prompt
                            },
                            {
                                "role": "user",
                                "content": patient_data
                            }
                        ],
                        temperature=0.3,
                        max_completion_tokens=4000
                    )

                    result = response.choices[0].message.content

                    st.session_state.analysis_result = result
                    st.session_state.patient_name = (
                        patient_name or "Unnamed Patient"
                    )

            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")

    # --------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------

    if st.session_state.analysis_result:

        st.divider()

        st.markdown("## Clinical Analysis")

        st.caption(
            f"Patient: {st.session_state.patient_name}  |  "
            f"Generated: {datetime.now().strftime('%d %B %Y, %I:%M %p')}"
        )

        with st.container(border=True):
            st.markdown(st.session_state.analysis_result)

        st.download_button(
            label="↓ Download Clinical Report",
            data=(
                "# CareLens Clinical Analysis\n\n"
                + st.session_state.analysis_result
            ),
            file_name="CareLens_Clinical_Report.md",
            mime="text/markdown",
            use_container_width=True
        )

        if st.button("Clear Analysis", use_container_width=True):
            st.session_state.analysis_result = None
            st.session_state.patient_name = ""
            st.rerun()


# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------

elif page == "About CareLens":

    st.markdown("## About CareLens")

    st.markdown("""
    CareLens is an AI-assisted clinical information platform
    designed to organize patient information and generate
    structured clinical insights.

    Its purpose is to make patient information easier to
    understand and help users explore relevant clinical
    considerations.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### Patient Assessment")
            st.write(
                "Collect and organize patient symptoms, medical "
                "history, and clinical measurements."
            )

        with st.container(border=True):
            st.markdown("### Clinical Insights")
            st.write(
                "Explore possible conditions, differential "
                "considerations, and relevant investigations."
            )

    with col2:
        with st.container(border=True):
            st.markdown("### AI-Powered Analysis")
            st.write(
                "Generate structured reports using Groq's "
                "language model infrastructure."
            )

        with st.container(border=True):
            st.markdown("### Report Generation")
            st.write(
                "Export generated clinical analysis for "
                "educational review."
            )

    st.divider()

    st.markdown("### Technology Stack")

    st.markdown("""
    - **Frontend:** Streamlit
    - **AI Infrastructure:** Groq API
    - **Language Model:** OpenAI GPT-OSS 120B
    - **Language:** Python
    """)

    st.warning("""
    **Medical Disclaimer**

    CareLens is an educational demonstration, not a medical
    device or substitute for professional healthcare.
    Its output may be incomplete or inaccurate. Do not use
    it to diagnose, prescribe, or make emergency-care decisions.
    Always consult a qualified healthcare professional.
    """)
