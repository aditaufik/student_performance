import streamlit as st
import pandas as pd
import joblib

# Load model dan encoder
model = joblib.load('model/model_rf.joblib')
label_encoder = joblib.load('model/label_encoder.joblib')

st.set_page_config(page_title="Student Dropout Prediction", layout="wide")
st.title("🎓 Jaya Jaya Institute Student Prediction")

with st.form("student_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        admission_grade = st.slider("Admission Grade", 80.0, 200.0, 120.0, help="Nilai ujian masuk siswa (80 - 200)")
        curricular_units_1st_sem_grade = st.slider("1st Sem Grade", 0.0, 20.0, 12.0, help="Rata-rata nilai semester 1")
        curricular_units_1st_sem_approved = st.slider("1st Sem Passed Courses", 0, 20, 4, help="Jumlah mata kuliah lulus semester 1")
        curricular_units_2nd_sem_grade = st.slider("2nd Sem Grade", 0.0, 20.0, 12.0, help="Rata-rata nilai semester 2")
        curricular_units_2nd_sem_approved = st.slider("2nd Sem Passed Courses", 0, 20, 4, help="Jumlah mata kuliah lulus semester 2")
        curricular_units_1st_sem_enrolled = st.slider("1st Sem Enrolled", 0, 20, 5, help="Jumlah mata kuliah semester 1")
        curricular_units_2nd_sem_enrolled = st.slider("2nd Sem Enrolled", 0, 23, 5, help="Jumlah mata kuliah semester 2")

    with col2:
        curricular_units_1st_sem_evaluations = st.slider("1st Sem Evaluations", 0, 30, 5, help="Evaluasi semester 1")
        curricular_units_2nd_sem_evaluations = st.slider("2nd Sem Evaluations", 0, 30, 5, help="Evaluasi semester 2")
        previous_qualification_grade = st.slider("Previous Qualification Grade", 95.0, 190.0, 120.0, help="Nilai pada pendidikan sebelumnya")
        unemployment_rate = st.slider("Unemployment Rate", 7.6, 16.2, 11.0, help="Tingkat pengangguran (7.6% - 16.2%)")
        gdp = st.slider("GDP", -4.06, 3.51, 1.0, help="Produk domestik bruto (pertumbuhan ekonomi)")
        inflation_rate = st.slider("Inflation Rate", -0.8, 3.7, 1.2, help="Tingkat inflasi tahunan (%)")
        tuition_fees_up_to_date = st.selectbox("Tuition Up to Date", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", help="Apakah siswa melunasi biaya kuliah?")
        scholarship_holder = st.selectbox("Scholarship Holder", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", help="Apakah siswa menerima beasiswa?")

    with col3:
        debtor = st.selectbox("Debtor", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", help="Apakah siswa memiliki hutang?")
        displaced = st.selectbox("Displaced", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", help="Apakah siswa berasal dari lokasi relokasi khusus?")
        gender = st.radio("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female", help="Jenis kelamin siswa")
        age_at_enrollment = st.slider("Age at Enrollment", 17, 70, 22, help="Usia saat pertama kali mendaftar kuliah")
        application_order = st.slider("Application Order", 0, 9, 1, help="Pilihan keberapa universitas ini (0-9)")
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
        }[x], help="Jenis jalur pendaftaran")

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
            19: "Basic Education 9-11",
            38: "Basic Education 6-8",
            39: "Tech Specialization",
            40: "Degree 1st Cycle",
            42: "Prof Higher Tech Course",
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
        }[x], help="Kualifikasi pendidikan sebelum mendaftar")

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
