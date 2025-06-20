import streamlit as st
import pandas as pd
import joblib
import io

# Load model and encoder
model = joblib.load('model/model_rf.joblib')
label_encoder = joblib.load('model/label_encoder.joblib')

st.set_page_config(page_title="Student Performance Prediction", layout="wide")
st.title("🎓 Student Performance Prediction")

with st.form("student_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.radio("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female", help="Gender of the student")
        age_at_enrollment = st.slider("Age at Enrollment", 17, 70, 22, help="Age when the student enrolled")
        application_order = st.slider("Application Order", 0, 9, 1, help="Order in which the student chose the course")
        application_mode = st.selectbox("Application Mode", {
            1: "1st Phase - General Contingent",
            5: "1st Phase - Azores",
            7: "Other Higher Courses",
            10: "Ordinance 854-B/99",
            15: "International Student",
            39: "Over 23 Years Old",
            42: "Transfer",
            43: "Change Course",
            44: "Tech Diploma Holders",
            51: "Institution/Course Change",
            57: "Intl Institution/Course Change"
        }.keys(), format_func=lambda x: {
            1: "1st Phase - General Contingent",
            5: "1st Phase - Azores",
            7: "Other Higher Courses",
            10: "Ordinance 854-B/99",
            15: "International Student",
            39: "Over 23 Years Old",
            42: "Transfer",
            43: "Change Course",
            44: "Tech Diploma Holders",
            51: "Institution/Course Change",
            57: "Intl Institution/Course Change"
        }[x], help="The method of application used by the student")

        previous_qualification = st.selectbox("Previous Qualification", {
            1: "Secondary Education",
            2: "Bachelor Degree",
            3: "Higher Degree",
            4: "Master",
            5: "Doctorate",
            6: "Freq Higher Ed",
            9: "12th Not Completed",
            12: "11th Schooling",
            14: "10th Schooling",
            15: "10th Not Completed",
            19: "Basic Ed 9-11",
            38: "Basic Ed 6-8",
            39: "Tech Specialization",
            40: "Degree 1st Cycle",
            42: "Prof Higher Tech",
            43: "Master 2nd Cycle"
        }.keys(), format_func=lambda x: {
            1: "Secondary Education",
            2: "Bachelor Degree",
            3: "Higher Degree",
            4: "Master",
            5: "Doctorate",
            6: "Freq Higher Ed",
            9: "12th Not Completed",
            12: "11th Schooling",
            14: "10th Schooling",
            15: "10th Not Completed",
            19: "Basic Ed 9-11",
            38: "Basic Ed 6-8",
            39: "Tech Specialization",
            40: "Degree 1st Cycle",
            42: "Prof Higher Tech",
            43: "Master 2nd Cycle"
        }[x], help="The qualification obtained before enrolling in higher education")
        
        debtor = st.selectbox("Debtor", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", help="Does the student have debts?")
        displaced = st.selectbox("Displaced", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", help="Is the student from a displaced region?")
        
    with col2:
        admission_grade = st.slider("Admission Grade", 80.0, 200.0, 120.0, help="The student's score on the admission exam (80 - 200)")
        curricular_units_1st_sem_grade = st.slider("1st Semester Grade", 0.0, 20.0, 12.0, help="Average grade in the 1st semester")
        curricular_units_1st_sem_approved = st.slider("1st Semester Passed Courses", 0, 26, 4, help="Number of courses passed in 1st semester")
        curricular_units_2nd_sem_grade = st.slider("2nd Semester Grade", 0.0, 20.0, 12.0, help="Average grade in the 2nd semester")
        curricular_units_2nd_sem_approved = st.slider("2nd Semester Passed Courses", 0, 20, 4, help="Number of courses passed in 2nd semester")
        curricular_units_1st_sem_enrolled = st.slider("1st Semester Enrolled Courses", 0, 26, 5, help="Number of courses enrolled in 1st semester")
        curricular_units_2nd_sem_enrolled = st.slider("2nd Semester Enrolled Courses", 0, 23, 5, help="Number of courses enrolled in 2nd semester")

    with col3:
        curricular_units_1st_sem_evaluations = st.slider("1st Semester Evaluations", 0, 45, 5, help="Number of evaluations in 1st semester")
        curricular_units_2nd_sem_evaluations = st.slider("2nd Semester Evaluations", 0, 33, 5, help="Number of evaluations in 2nd semester")
        previous_qualification_grade = st.slider("Previous Qualification Grade", 95.0, 190.0, 120.0, help="Grade obtained in previous education")
        unemployment_rate = st.slider("Unemployment Rate", 7.0, 17.0, 11.0, help="National unemployment rate at the time")
        gdp = st.slider("GDP Growth", -4.00, 4.00, 1.0, help="Gross Domestic Product growth (%)")
        inflation_rate = st.slider("Inflation Rate", -0.0, 4.0, 1.2, help="National inflation rate (%)")
        tuition_fees_up_to_date = st.selectbox("Tuition Fees Up To Date", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", help="Is the student's tuition paid up to date?")
        scholarship_holder = st.selectbox("Scholarship Holder", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", help="Does the student receive a scholarship?")

    submitted = st.form_submit_button("🔍 Predict")

if submitted:
        data = pd.DataFrame({
            'Admission_grade': [admission_grade],
            'Age_at_enrollment': [age_at_enrollment],
            'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
            'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
            'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
            'Curricular_units_1st_sem_enrolled': [curricular_units_1st_sem_enrolled],
            'Curricular_units_2nd_sem_enrolled': [curricular_units_2nd_sem_enrolled],
            'Curricular_units_1st_sem_evaluations': [curricular_units_1st_sem_evaluations],
            'Curricular_units_2nd_sem_evaluations': [curricular_units_2nd_sem_evaluations],
            'Previous_qualification_grade': [previous_qualification_grade],
            'Unemployment_rate': [unemployment_rate],
            'GDP': [gdp],
            'Inflation_rate': [inflation_rate],
            'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
            'Scholarship_holder': [scholarship_holder],
            'Debtor': [debtor],
            'Displaced': [displaced],
            'Gender': [gender],
            'Application_order': [application_order],
            'Application_mode': [application_mode],
            'Previous_qualification': [previous_qualification],
        })

        data = pd.get_dummies(data)
        for col in model.feature_names_in_:
            if col not in data.columns:
                data[col] = 0
        data = data[model.feature_names_in_]
        pred = model.predict(data)
        label = label_encoder.inverse_transform(pred)[0]

        st.success(f"📘 Prediction Result: **{label}**")

        result_df = data.copy()
        result_df['Prediction'] = label
        csv = result_df.to_csv(index=False)
        
        st.download_button(
            label="📥 Download Prediction as CSV",
            data=csv,
            file_name='student_prediction.csv',
            mime='text/csv'
        )
