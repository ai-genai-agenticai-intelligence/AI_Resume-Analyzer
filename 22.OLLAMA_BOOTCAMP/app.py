import streamlit as st
from pdf_reader import extract_text
from analyzer import analyze_resume

st.set_page_config(page_title="Resume Analyzer", page_icon=":bar_chart:", layout="wide")

st.title("AI-POWERED RESUME ANALYZER")
st.write("This app analyzes resumes and provides insights into the candidate's qualifications, skills, and experience.")

uploaded_file = st.file_uploader("Upload a resume (PDF format)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    if st.button("Show Analysis Result"):
        with st.spinner('Analyzing the resume...'):
            result = analyze_resume(resume_text)
        st.success("Analysis complete!")
        st.markdown("### Resume Analysis Result")
        st.text(result)
        st.download_button(
            label="Download Analysis Result",
            data=result,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )
			 
