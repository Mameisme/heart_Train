'''import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the machine learning model and encode
model = joblib.load('heartDis.joblib.joblib')


def main():
    st.title('Churn Model Deployment')

    # Add user input components for 10 features
    #input one by one
    age=st.number_input("age", 0, 100)
    gender=st.radio("gender", ["Male","Female"])
    tenure=st.number_input("the period of time you holds a position (in years)", 0,100)
    usage_freq=st.number_input("the frequency of product usage (in years)", 0,100)
    support_call=st.number_input("number of support calls", 0,10)
    payment_delay=st.number_input("the period of payment delay (in months)", 0,30)
    subs_type=st.radio("choose subscription type", ["Standard","Premium","Basic"])
    contract_length=st.radio("choose contract length", ["Annual","Quarterly","Monthly"])
    total_spend=st.number_input("total spend in a month", 0,1000000000)
    last_interaction=st.number_input("last interaction with the product (in months)", 0,30)
    
    
    data = {'Age': int(age), 'Gender': gender, 'Tenure':int(tenure),'Usage Frequency':int(usage_freq),
            'Support Calls': int(support_call), 'Payment Delay':int(payment_delay),
            'Subscription Type':subs_type, 'Contract Length': contract_length,
            'Total Spend':int(total_spend),'Last Interaction':int(last_interaction)}
    
    df=pd.DataFrame([list(data.values())], columns=['Age','Gender', 'Tenure', 'Usage Frequency','Support Calls', 
                                                'Payment Delay', 'Subscription Type','Contract Length', 
                                                'Total Spend', 'Last Interaction'])

    df=df.rename(columns={"Usage Frequency": "UsageFrequency", "Support Calls": "SupportCalls", 
                   "Payment Delay": "PaymentDelay","Subscription Type":"SubscriptionType",
                   "Contract Length": "ContractLength" , "Total Spend":  "TotalSpend", 
                   "Last Interaction":"LastInteraction" })
    
    
    if st.button("Make Prediction"):
        prediction = model.predict(df)[0]

        if prediction == 0:
            result = "Not Churn"
        else:
            result = "Churn"

        st.success(f"Churn Prediction: {result}")


if __name__ == "__main__":
    main()'''


import streamlit as st
import pandas as pd

model = joblib.load('heartDis.joblib.joblib')

def main():
    st.title('Churn Model Deployment')
    
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

if __name__ == "__main__":
    main()