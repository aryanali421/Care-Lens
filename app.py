
import streamlit as st
from groq import Groq
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="CareLens | Clinical Intelligence",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# MEDICAL UI DESIGN
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f4f8fb;
}

[data-testid="stHeader"] {
    background: rgba(244,248,251,0.9);
}

[data-testid="stSidebar"] {
    background: #102d40;
}

[data-testid="stSidebar"] * {
    color: #eaf4f8 !important;
}

[data-testid="stSidebar"] .stButton button {
    background: #147d83;
    color: white !important;
    border: none;
}

.hero {
    background: linear-gradient(115deg, #102f45, #176c72);
    padding: 30px 34px;
    border-radius: 18px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 8px 25px rgba(16,47,69,0.12);
}

.hero h1 {
    color: white;
    font-family: 'Manrope', sans-serif;
    font-size: 34px;
    font-weight: 800;
    margin: 0;
}

.hero p {
    color: #d5e9eb;
    margin: 7px 0 0 0;
    font-size: 15px;
}

.section-title {
    color: #17394d;
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
    font-size: 21px;
    margin: 15px 0;
}

.metric-card {
    background: white;
    border: 1px solid #e3edf2;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 3px 12px rgba(20,55,75,0.04);
    min-height: 105px;
}

.metric-label {
    color: #718596;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .6px;
}

.metric-value {
    color: #17394d;
    font-family: 'Manrope', sans-serif;
    font-size: 24px;
    font-weight: 800;
    margin-top: 8px;
}

.info-box {
    background: #eaf5f6;
    border-left: 4px solid #16858a;
    padding: 14px 17px;
    border-radius: 8px;
    color: #24515b;
    font-size: 13px;
    margin: 15px 0;
}

.warning-box {
    background: #fff7e9;
    border-left: 4px solid #e2a43b;
    padding: 14px 17px;
    border-radius: 8px;
    color: #79551d;
    font-size: 13px;
    margin: 15px 0;
}

.stButton > button {
    border-radius: 9px;
    min-height: 44px;
    font-weight: 700;
    transition: all .2s ease;
}

.stButton > button[kind="primary"] {
    background: #147d83;
    border: none;
}

.stButton > button[kind="primary"]:hover {
    background: #10676d;
    transform: translateY(-1px);
}

div[data-testid="stForm"] {
    background: white;
    border: 1px solid #e3edf2;
    padding: 22px;
    border-radius: 15px;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 15px;
}

.stTabs [data-baseweb="tab"] {
    font-weight: 700;
}

[data-testid="stTextArea"] textarea,
[data-testid="stTextInput"] input {
    border-radius: 9px;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# API CONFIGURATION
# --------------------------------------------------

def get_groq_key():
    try:
        return st.secrets["GROQ_API_KEY"]
    except (KeyError, FileNotFoundError):
        return None


api_key = get_groq_key()

MODEL = "llama-3.3-70b-versatile"


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("""
    <div style="text-align:center;padding:15px 5px 25px;">
        <div style="font-size:42px;">🩺</div>
        <div style="font-size:25px;font-weight:800;
                    font-family:Manrope;color:white;">
            CareLens
        </div>
        <div style="font-size:11px;color:#a9c6d1;">
            CLINICAL INTELLIGENCE PLATFORM
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### Navigation")

    page = st.radio(
        "Navigate",
        ["Patient Analysis", "About CareLens"],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### System Status")

    if api_key:
        st.success("Groq AI connected")
    else:
        st.error("API key not configured")

    st.caption(f"Model: {MODEL}")

    st.divider()

    st.markdown("### Privacy & Safety")
    st.caption(
        "Use fictional or properly de-identified information. "
        "Patient information should not contain names, addresses, "
        "phone numbers or identification numbers."
    )

    st.markdown("""
    <div style="font-size:11px;color:#a9c6d1;
                margin-top:30px;">
        CARELENS • STUDENT PROJECT<br>
        AI-ASSISTED HEALTHCARE
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <div style="font-size:12px;letter-spacing:1.5px;
                color:#a9d9d9;font-weight:700;">
        HEALTHCARE • ARTIFICIAL INTELLIGENCE
    </div>
    <h1>Clinical Intelligence Dashboard</h1>
    <p>
        Analyse patient information, identify potential health
        concerns and support informed clinical decisions.
    </p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PATIENT ANALYSIS PAGE
# --------------------------------------------------

if page == "Patient Analysis":

    st.markdown(
        '<div class="section-title">Patient Overview</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">AI Engine</div>
            <div class="metric-value">Groq AI</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Analysis Type</div>
            <div class="metric-value">Clinical Support</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Platform Status</div>
            <div class="metric-value">Active</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Patient Information</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        Enter patient information below. For this demonstration,
        use fictional or de-identified patient records.
    </div>
    """, unsafe_allow_html=True)

    with st.form("patient_form"):

        st.markdown("#### Basic Information")

        c1, c2, c3 = st.columns(3)

        with c1:
            age = st.number_input(
                "Patient Age",
                min_value=0,
                max_value=120,
                value=35
            )

        with c2:
            sex = st.selectbox(
                "Sex",
                ["Not specified", "Male", "Female", "Other"]
            )

        with c3:
            duration = st.text_input(
                "Symptom Duration",
                placeholder="e.g. 5 days"
            )

        st.divider()

        st.markdown("#### Clinical Information")

        symptoms = st.text_area(
            "Current Symptoms",
            placeholder=(
                "Describe symptoms, severity and when they started..."
            ),
            height=120
        )

        medical_history = st.text_area(
            "Medical History",
            placeholder=(
                "Previous illnesses, surgeries, existing conditions..."
            ),
            height=100
        )

        medications = st.text_area(
            "Medications and Allergies",
            placeholder=(
                "Current medications and known allergies..."
            ),
            height=90
        )

        st.divider()

        st.markdown("#### Observations & Test Results")

        vitals = st.text_area(
            "Vital Signs",
            placeholder=(
                "Blood pressure, temperature, pulse, oxygen saturation..."
            ),
            height=90
        )

        tests = st.text_area(
            "Laboratory Results / Medical Reports",
            placeholder=(
                "Blood glucose, HbA1c, cholesterol, blood count..."
            ),
            height=100
        )

        st.divider()

        st.markdown("#### Analysis Preferences")

        analysis_type = st.multiselect(
            "Select analysis areas",
            [
                "Patient Information Summary",
                "Potential Health Risks",
                "Missing Clinical Information",
                "Further Investigation Considerations",
                "Treatment Support Strategies",
                "Preventive Healthcare",
                "AI Benefits and Limitations"
            ],
            default=[
                "Patient Information Summary",
                "Potential Health Risks",
                "Missing Clinical Information",
                "Treatment Support Strategies"
            ]
        )

        submitted = st.form_submit_button(
            "✦ Analyse Patient Information",
            type="primary",
            use_container_width=True
        )


    # --------------------------------------------------
    # AI ANALYSIS
    # --------------------------------------------------

    if submitted:

        if not api_key:
            st.error(
                "Groq API key is missing. Add GROQ_API_KEY "
                "in your Streamlit Secrets settings."
            )

        elif not symptoms.strip() and not vitals.strip() and not tests.strip():
            st.warning(
                "Please enter some patient information before analysis."
            )

        elif not analysis_type:
            st.warning("Please select at least one analysis area.")

        else:

            prompt = f"""
You are an educational AI healthcare support assistant.

Review the following fictional or de-identified patient information.

PATIENT DETAILS
Age: {age}
Sex: {sex}
Symptom duration: {duration}

SYMPTOMS
{symptoms}

MEDICAL HISTORY
{medical_history}

MEDICATIONS AND ALLERGIES
{medications}

VITAL SIGNS
{vitals}

LABORATORY RESULTS
{tests}

REQUESTED ANALYSIS
{", ".join(analysis_type)}

IMPORTANT MEDICAL SAFETY RULES:

1. Do not claim to diagnose or confirm a disease.
2. Do not prescribe medications or dosages.
3. Do not recommend starting or stopping medication.
4. Distinguish known facts from possible concerns.
5. Never invent missing medical information.
6. Explain uncertainty and limitations.
7. Identify potentially urgent warning signs.
8. If the information suggests an emergency, clearly advise
   immediate emergency medical assessment.
9. Treatment suggestions must remain general and subject
   to qualified medical review.
10. Do not calculate unsupported medical risk scores.

STRUCTURE YOUR RESPONSE:

### 1. Patient Summary
Summarise the available patient information.

### 2. Potential Health Risks
Highlight possible concerns and explain why they may
need further clinical assessment. Do not diagnose.

### 3. Missing Information
Identify information that would help the medical team.

### 4. Further Investigation
Suggest possible questions, examinations or tests
for a qualified clinician to consider.

### 5. Treatment Support Strategies
Provide general patient-support and care-planning
considerations for medical professionals to review.

### 6. Preventive Healthcare
Mention relevant general lifestyle and monitoring
considerations where appropriate.

### 7. AI Limitations
Explain why clinical verification and human judgement
remain necessary.

Use clear headings, concise explanations and professional
medical language.
"""

            try:

                client = Groq(api_key=api_key)

                with st.spinner(
                    "CareLens is reviewing patient information..."
                ):

                    response = client.chat.completions.create(
                        model=MODEL,
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are a cautious educational "
                                    "healthcare information assistant. "
                                    "You do not replace licensed clinicians."
                                )
                            },
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],
                        temperature=0.2,
                        max_tokens=2200
                    )

                    result = response.choices[0].message.content

                    st.session_state["analysis_result"] = result
                    st.session_state["analysis_date"] = (
                        datetime.now().strftime("%d %B %Y, %I:%M %p")
                    )

                st.success("Patient information review completed.")

            except Exception as e:
                st.error(f"Analysis failed: {e}")


    # --------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------

    if st.session_state.get("analysis_result"):

        st.divider()

        st.markdown(
            '<div class="section-title">Clinical Analysis Report</div>',
            unsafe_allow_html=True
        )

        st.caption(
            "Generated on: "
            + st.session_state.get("analysis_date", "")
        )

        st.markdown("""
        <div class="info-box">
            AI-generated clinical support information.
            Findings are not confirmed diagnoses and require
            independent medical review.
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs([
            "📋 Analysis Report",
            "📄 Export Report"
        ])

        with tab1:
            st.markdown(
                st.session_state["analysis_result"]
            )

        with tab2:

            st.markdown("### Download Patient Report")

            st.download_button(
                "⬇ Download Report",
                data=st.session_state["analysis_result"],
                file_name="CareLens_Clinical_Report.txt",
                mime="text/plain",
                use_container_width=True
            )

            st.caption(
                "The downloaded report is an educational AI-generated "
                "summary, not an official medical record."
            )


# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------

elif page == "About CareLens":

    st.markdown("## About CareLens")

    st.write("""
    CareLens is an AI-assisted healthcare demonstration
    designed to show how artificial intelligence can support
    hospitals in reviewing patient information and planning care.

    It uses the Groq API to process clinical information and
    generate structured educational reports.
    """)

    st.markdown("### Main Features")

    features = [
        ("Patient Analysis", "Organises symptoms, medical history and observations."),
        ("Risk Identification", "Highlights potential health concerns for clinician review."),
        ("Treatment Support", "Provides general care-planning considerations."),
        ("Preventive Healthcare", "Identifies relevant monitoring and lifestyle considerations."),
        ("Clinical Reports", "Generates downloadable patient analysis summaries.")
    ]

    for title, description in features:
        with st.expander(title):
            st.write(description)

    st.markdown("### Technology Stack")

    st.write("""
    - Python
    - Streamlit
    - Groq API
    - Llama 3.3 70B
    """)

    st.markdown("### Benefits of AI")

    st.write("""
    AI can save time, organise large amounts of information,
    highlight patterns and support medical professionals
    in making informed decisions.
    """)

    st.markdown("### Limitations")

    st.write("""
    AI can produce inaccurate information, reflect biases
    in its training data and overlook important clinical context.
    It cannot replace doctors or independent medical judgement.
    """)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown("""
<div style="text-align:center;padding:12px;color:#8296a5;
            font-size:12px;">
    <b>CareLens</b> · AI-Assisted Healthcare Support<br>
    Built with Streamlit and Groq · Educational Prototype<br><br>
    Not intended for real-world diagnosis or treatment.
</div>
""", unsafe_allow_html=True)
