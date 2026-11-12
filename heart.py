

import streamlit as st
import pandas as pd
import joblib

model = joblib.load('heartDis.joblib')

    
# Konfigurasi halaman
st.set_page_config(
    page_title="Heart Disease Input",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ Heart Disease Prediction")
st.subheader("Input Data Pasien")

st.write("Silakan masukkan data pasien berikut.")

# Form input
with st.form("input_pasien"):

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=45
        )

        sex = st.selectbox(
            "Sex",
            ["Male", "Female"]
        )

        dataset = st.selectbox(
            "Dataset",
            ["Cleveland", "Hungary",
             "Switzerland", "VA Long Beach"]
        )

        cp = st.selectbox(
            "Chest Pain Type (CP)",
            [
                "typical angina",
                "atypical angina",
                "non-anginal",
                "asymptomatic"
            ]
        )

        trestbps = st.number_input(
            "Resting Blood Pressure",
            min_value=0,
            max_value=300,
            value=120
        )

        chol = st.number_input(
            "Cholesterol",
            min_value=0,
            max_value=700,
            value=200
        )

    with col2:
        fbs = st.selectbox(
            "Fasting Blood Sugar",
            [True, False]
        )

        restecg = st.selectbox(
            "Resting ECG",
            [
                "normal",
                "st-t abnormality",
                "lv hypertrophy"
            ]
        )

        thalch = st.number_input(
            "Maximum Heart Rate",
            min_value=0,
            max_value=250,
            value=150
        )

        exang = st.selectbox(
            "Exercise Induced Angina",
            [True, False]
        )

        oldpeak = st.number_input(
            "Oldpeak",
            min_value=-5.0,
            max_value=10.0,
            value=1.0,
            step=0.1
        )

    # Tombol submit
    submit = st.form_submit_button(
        "Simpan Input",
        use_container_width=True
    )

# Menampilkan hasil input
if submit:

    input_data = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "dataset": dataset,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalch": thalch,
        "exang": exang,
        "oldpeak": oldpeak
    }])

    st.success("Data berhasil dimasukkan!")

    st.subheader("Data Pasien")
    st.dataframe(
        input_data,
        use_container_width=True,
        hide_index=True
    )

    st.write("Data siap digunakan untuk prediksi Machine Learning.")
