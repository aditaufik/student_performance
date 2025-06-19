import streamlit as st
import pandas as pd
import joblib

# Load model dan encoder
model = joblib.load('model_rf.joblib')
label_encoder = joblib.load('label_encoder.joblib')

st.set_page_config(page_title="Dropout Predictor App", layout="wide")
st.title("🎓 Student Dropout Prediction")
st.markdown("Gunakan aplikasi ini untuk memprediksi status siswa berdasarkan data pendaftaran dan performa awal.")

# UI Layout
with st.form("student_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        admission_grade = st.slider("Nilai Masuk", 0.0, 200.0, 120.0)
        age_at_enrollment = st.slider("Usia Saat Mendaftar", 17, 70, 22)
        curricular_units_1st_sem_grade = st.slider("Rata-rata Nilai Semester 1", 0.0, 20.0, 12.0)
        curricular_units_1st_sem_approved = st.slider("Jumlah Mata Kuliah Lulus Semester 1", 0, 20, 4)
        curricular_units_2nd_sem_grade = st.slider("Rata-rata Nilai Semester 2", 0.0, 20.0, 12.0)

    with col2:
        curricular_units_1st_sem_enrolled = st.slider("Jumlah Mata Kuliah Semester 1", 0, 20, 5)
        curricular_units_1st_sem_evaluations = st.slider("Evaluasi Semester 1", 0, 30, 5)
        curricular_units_2nd_sem_approved = st.slider("Jumlah Mata Kuliah Lulus Semester 2", 0, 20, 4)
        curricular_units_2nd_sem_evaluations = st.slider("Evaluasi Semester 2", 0, 30, 5)
        previous_qualification_grade = st.slider("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 120.0)
        unemployment_rate = st.slider("Tingkat Pengangguran", 0.0, 20.0, 5.0)
        gdp = st.slider("GDP", -5.0, 5.0, 1.0)
        inflation_rate = st.slider("Inflasi", 0.0, 20.0, 3.0)


    with col3:
        tuition_fees_up_to_date = st.selectbox("Pembayaran Lunas", [0, 1])
        scholarship_holder = st.selectbox("Penerima Beasiswa", [0, 1])
        debtor = st.selectbox("Memiliki Hutang", [0, 1])
        gender = st.selectbox("Jenis Kelamin", [0, 1], format_func=lambda x: "Laki-laki" if x == 0 else "Perempuan")
        displaced = st.selectbox("Displaced", [0, 1])
        application_order = st.slider("Urutan Aplikasi", 1, 20, 1)
        application_mode = st.selectbox("Mode Aplikasi", [1, 5, 7, 10, 15, 39, 42, 43, 44, 51, 57])
        previous_qualification = st.selectbox("Kualifikasi Sebelumnya", [1, 2, 3, 4, 5, 6, 9, 12])


    submitted = st.form_submit_button("🔍 Prediksi")

    if submitted:
        # Buat DataFrame
        data = pd.DataFrame({
            'Admission_grade': [admission_grade],
            'Age_at_enrollment': [age_at_enrollment],
            'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
            'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
            'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
            'Curricular_units_1st_sem_enrolled': [curricular_units_1st_sem_enrolled],
            'Curricular_units_1st_sem_evaluations': [curricular_units_1st_sem_evaluations],
            'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
            'Previous_qualification_grade': [previous_qualification_grade],
            'Unemployment_rate': [unemployment_rate],
            'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
            'Scholarship_holder': [scholarship_holder],
            'Debtor': [debtor],
            'Gender': [gender],
            'Displaced': [displaced],
            'Curricular_units_2nd_sem_evaluations': [curricular_units_2nd_sem_evaluations],
            'GDP': [gdp],
            'Inflation_rate': [inflation_rate],
            'Application_order': [application_order],
            'Application_mode': [application_mode],
            'Previous_qualification': [previous_qualification],
        })

        # Pastikan fitur sesuai model
        data = pd.get_dummies(data)
        model_features = model.feature_names_in_
        for col in model_features:
            if col not in data.columns:
                data[col] = 0
        data = data[model_features]

        # Prediksi
        pred = model.predict(data)
        label = label_encoder.inverse_transform(pred)[0]

        st.success(f"📘 Status Prediksi: **{label}**")
