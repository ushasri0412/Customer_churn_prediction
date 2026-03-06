import streamlit as st
import pickle
import numpy as np

# Load model
with open("logistic_model.pkl","rb") as f:
    model = pickle.load(f)

# Load scaler
with open("scaler.pkl","rb") as f:
    scaler = pickle.load(f)

st.set_page_config(page_title="Customer Churn Prediction",
                   page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUFn08nPcyt3DsaFCFJ4tQxaV9AW3cmf56Jw&s")
# Center Title
st.markdown(
    "<h1 style='text-align: center;'>Customer Churn Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align: center;'>Predicting whether a customer will churn or stay</h4>",
    unsafe_allow_html=True
)

# Center Image 
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(
        "https://www.hashstudioz.com/blog/wp-content/uploads/2025/02/Churn-Prediction-in-Retail-How-Data-Analytics-Improves-Customer-Retention-1.png",
        width=350
    )

st.write("")

# Two Column Layout 
col1, col2 = st.columns(2)

with col1:

    gender = st.radio("Gender", ["Female","Male"])
    senior = st.radio("Senior Citizen", ["No","Yes"])
    partner = st.radio("Partner", ["No","Yes"])
    dependents = st.radio("Dependents", ["No","Yes"])

    tenure = st.number_input("Tenure (months)", min_value=0)

    phoneservice = st.radio("Phone Service", ["No","Yes"])
    paperless = st.radio("Paperless Billing", ["No","Yes"])

with col2:

    multiplelines = st.selectbox(
        "Multiple Lines",
        ["No","Yes","No phone service"]
    )

    internetservice = st.selectbox(
        "Internet Service",
        ["DSL","Fiber optic","No"]
    )

    onlinesecurity = st.selectbox(
        "Online Security",
        ["No","Yes","No internet service"]
    )

    onlinebackup = st.selectbox(
        "Online Backup",
        ["No","Yes","No internet service"]
    )

    deviceprotection = st.selectbox(
        "Device Protection",
        ["No","Yes","No internet service"]
    )

    techsupport = st.selectbox(
        "Tech Support",
        ["No","Yes","No internet service"]
    )

    streamingtv = st.selectbox(
        "Streaming TV",
        ["No","Yes","No internet service"]
    )

    streamingmovies = st.selectbox(
        "Streaming Movies",
        ["No","Yes","No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month","One year","Two year"]
    )

    paymentmethod = st.selectbox(
        "Payment Method",
        ["Electronic check","Mailed check","Bank transfer","Credit card"]
    )

    monthlycharges = st.number_input("Monthly Charges")
    totalcharges = st.number_input("Total Charges")

# Convert Inputs to Numbers

gender = 1 if gender=="Male" else 0
senior = 1 if senior=="Yes" else 0
partner = 1 if partner=="Yes" else 0
dependents = 1 if dependents=="Yes" else 0
phoneservice = 1 if phoneservice=="Yes" else 0
paperless = 1 if paperless=="Yes" else 0

multiplelines = ["No","Yes","No phone service"].index(multiplelines)
internetservice = ["DSL","Fiber optic","No"].index(internetservice)

onlinesecurity = ["No","Yes","No internet service"].index(onlinesecurity)
onlinebackup = ["No","Yes","No internet service"].index(onlinebackup)
deviceprotection = ["No","Yes","No internet service"].index(deviceprotection)
techsupport = ["No","Yes","No internet service"].index(techsupport)

streamingtv = ["No","Yes","No internet service"].index(streamingtv)
streamingmovies = ["No","Yes","No internet service"].index(streamingmovies)

contract = ["Month-to-month","One year","Two year"].index(contract)

paymentmethod = ["Electronic check","Mailed check","Bank transfer","Credit card"].index(paymentmethod)

#Center Predict Button

c1, c2, c3 = st.columns([1,2,1])

with c2:
    predict = st.button("Predict Churn")

# Prediction 

if predict:

    input_data = np.array([[gender, senior, partner, dependents,
                            tenure, phoneservice, multiplelines,
                            internetservice, onlinesecurity,
                            onlinebackup, deviceprotection,
                            techsupport, streamingtv,
                            streamingmovies, contract,
                            paperless, paymentmethod,
                            monthlycharges, totalcharges]])

    # scale numerical columns
    input_data[:,[4,17,18]] = scaler.transform(input_data[:,[4,17,18]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer will Stay (No Churn)")