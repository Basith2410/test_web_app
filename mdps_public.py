# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 17:07:03 2023

@author: Mars
"""

import pickle
import streamlit as st
import pdfplumber
import re
from streamlit_option_menu import option_menu

# Set the background color and text color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0; /* Change the background color */
        color: #333; /* Change the text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom CSS for the title and sidebar
st.markdown(
    """
    <style>
    .stApp {
        max-width: 1200px; /* Adjust the maximum width of the app */
    }
    .stSidebar {
        background-color: #333; /* Change the sidebar background color */
        color: #fff; /* Change the sidebar text color */
    }
    .stSidebar option {
        background-color: #444; /* Change the sidebar dropdown background color */
        color: #fff; /* Change the sidebar dropdown text color */
    }
    .st-hv .sidebar-content {
        color: #fff; /* Change the active sidebar item text color */
    }
    .st-hv .sidebar-content::before {
        background-color: #fff; /* Change the active sidebar item indicator color */
    }
    .css-17eq0hr option {
        background-color: #fff; /* Change the dropdown menu background color */
        color: #333; /* Change the dropdown menu text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# loading the saved models

diabetes_model = pickle.load(open('diabetes.sav', 'rb'))

heart_disease_model = pickle.load(open('heartdisease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinson_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)

# Function to extract value from the report content based on the keyword
def extract_value(report_text, keyword):
    pattern = re.compile(rf'{keyword}\s*:\s*([\d.]+)')
    match = pattern.search(report_text)
    if match:
        return match.group(1)
    return ''

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Allow the user to upload a PDF report
    uploaded_file = st.file_uploader("Upload a PDF report", type=["pdf"])

    # Initialize variables to store extracted values
    extracted_values = {'Pregnancies': '', 'Glucose': '', 'BloodPressure': '', 'SkinThickness': '',
                        'Insulin': '', 'BMI': '', 'DiabetesPedigreeFunction': '', 'Age': ''}

    if uploaded_file is not None:
        pdf_text = ""
        try:
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    pdf_text += page.extract_text()
            extracted_values['Pregnancies'] = extract_value(pdf_text, 'Pregnancies')
            extracted_values['Glucose'] = extract_value(pdf_text, 'Glucose')
            extracted_values['BloodPressure'] = extract_value(pdf_text, 'BloodPressure')
            extracted_values['SkinThickness'] = extract_value(pdf_text, 'SkinThickness')
            extracted_values['Insulin'] = extract_value(pdf_text, 'Insulin')
            extracted_values['BMI'] = extract_value(pdf_text, 'BMI')
            extracted_values['DiabetesPedigreeFunction'] = extract_value(pdf_text, 'DiabetesPedigreeFunction')
            extracted_values['Age'] = extract_value(pdf_text, 'Age')
            #st.write("Extracted Values:", extracted_values)  # Debugging line
        except Exception as e:
            st.error(f"Error during PDF extraction: {e}")

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Pregnancies', value=extracted_values['Pregnancies'])

    with col2:
        Glucose = st.text_input('Glucose Level', value=extracted_values['Glucose'])

    with col3:
        BloodPressure = st.text_input('Blood Pressure', value=extracted_values['BloodPressure'])

    # Add input fields for the remaining columns
    with col1:
        SkinThickness = st.text_input('Skin Thickness', value=extracted_values['SkinThickness'])

    with col2:
        Insulin = st.text_input('Insulin Level', value=extracted_values['Insulin'])

    with col3:
        BMI = st.text_input('BMI', value=extracted_values['BMI'])

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function', value=extracted_values['DiabetesPedigreeFunction'])

    with col2:
        Age = st.text_input('Age of the Person', value=extracted_values['Age'])

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')

    # Allow the user to upload a PDF report
    uploaded_file = st.file_uploader("Upload a PDF report", type=["pdf"])

    # Initialize variables to store extracted values
    extracted_values = {'age': '', 'sex': '', 'cp': '', 'trestbps': '',
                        'chol': '', 'fbs': '', 'restecg': '', 'thalach': '',
                        'exang': '', 'oldpeak': '', 'slope': '', 'ca': '', 'thal': ''}

    if uploaded_file is not None:
        pdf_text = ""
        try:
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    pdf_text += page.extract_text()
            extracted_values['age'] = extract_value(pdf_text, 'age')
            extracted_values['sex'] = extract_value(pdf_text, 'sex')
            extracted_values['cp'] = extract_value(pdf_text, 'cp')
            extracted_values['trestbps'] = extract_value(pdf_text, 'trestbps')
            extracted_values['chol'] = extract_value(pdf_text, 'chol')
            extracted_values['fbs'] = extract_value(pdf_text, 'fbs')
            extracted_values['restecg'] = extract_value(pdf_text, 'restecg')
            extracted_values['thalach'] = extract_value(pdf_text, 'thalach')
            extracted_values['exang'] = extract_value(pdf_text, 'exang')
            extracted_values['oldpeak'] = extract_value(pdf_text, 'oldpeak')
            extracted_values['slope'] = extract_value(pdf_text, 'slope')
            extracted_values['ca'] = extract_value(pdf_text, 'ca')
            extracted_values['thal'] = extract_value(pdf_text, 'thal')
        except Exception as e:
            st.error(f"Error during PDF extraction: {e}")

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', value=extracted_values['age'])

    with col2:
        sex = st.text_input('Sex', value=extracted_values['sex'])

    with col3:
        cp = st.text_input('Chest pain types', value=extracted_values['cp'])

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', value=extracted_values['trestbps'])

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', value=extracted_values['chol'])

    with col3:
        fbs = st.text_input('Fasting Blood Sugar', value=extracted_values['fbs'])

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', value=extracted_values['restecg'])

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', value=extracted_values['thalach'])

    with col3:
        exang = st.text_input('Exercise Induced Angina', value=extracted_values['exang'])

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', value=extracted_values['oldpeak'])

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', value=extracted_values['slope'])

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', value=extracted_values['ca'])

    with col1:
        thal = st.text_input('Thal:', value=extracted_values['thal'])

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                                                        exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


# Parkinson's Disease Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Allow the user to upload a PDF report
    uploaded_file = st.file_uploader("Upload a PDF report", type=["pdf"])

    # Initialize variables to store extracted values
    extracted_values = {"MDVP:Fo(Hz)": "", "MDVP:Fhi(Hz)": "", "MDVP:Flo(Hz)": "", "MDVP:Jitter(%)": "",
                        "MDVP:Jitter(Abs)": "", "MDVP:RAP": "", "MDVP:PPQ": "", "Jitter:DDP": "",
                        "MDVP:Shimmer": "", "MDVP:Shimmer(dB)": "", "Shimmer:APQ3": "", "Shimmer:APQ5": "",
                        "MDVP:APQ": "", "Shimmer:DDA": "", "NHR": "", "HNR": "", "RPDE": "",
                        "DFA": "", "spread1": "", "spread2": "", "D2": "", "PPE": ""}

    if uploaded_file is not None:
        pdf_text = ""
        try:
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    pdf_text += page.extract_text()
            extracted_values["MDVP:Fo(Hz)"] = extract_value(pdf_text, "MDVP:Fo(Hz)")
            extracted_values["MDVP:Fhi(Hz)"] = extract_value(pdf_text, "MDVP:Fhi(Hz)")
            extracted_values["MDVP:Flo(Hz)"] = extract_value(pdf_text, "MDVP:Flo(Hz)")
            extracted_values["MDVP:Jitter(%)"] = extract_value(pdf_text, "MDVP:Jitter(%)")
            extracted_values["MDVP:Jitter(Abs)"] = extract_value(pdf_text, "MDVP:Jitter(Abs)")
            extracted_values["MDVP:RAP"] = extract_value(pdf_text, "MDVP:RAP")
            extracted_values["MDVP:PPQ"] = extract_value(pdf_text, "MDVP:PPQ")
            extracted_values["Jitter:DDP"] = extract_value(pdf_text, "Jitter:DDP")
            extracted_values["MDVP:Shimmer"] = extract_value(pdf_text, "MDVP:Shimmer")
            extracted_values["MDVP:Shimmer(dB)"] = extract_value(pdf_text, "MDVP:Shimmer(dB)")
            extracted_values["Shimmer:APQ3"] = extract_value(pdf_text, "Shimmer:APQ3")
            extracted_values["Shimmer:APQ5"] = extract_value(pdf_text, "Shimmer:APQ5")
            extracted_values["MDVP:APQ"] = extract_value(pdf_text, "MDVP:APQ")
            extracted_values["Shimmer:DDA"] = extract_value(pdf_text, "Shimmer:DDA")
            extracted_values["NHR"] = extract_value(pdf_text, "NHR")
            extracted_values["HNR"] = extract_value(pdf_text, "HNR")
            extracted_values["RPDE"] = extract_value(pdf_text, "RPDE")
            extracted_values["DFA"] = extract_value(pdf_text, "DFA")
            extracted_values["spread1"] = extract_value(pdf_text, "spread1")
            extracted_values["spread2"] = extract_value(pdf_text, "spread2")
            extracted_values["D2"] = extract_value(pdf_text, "D2")
            extracted_values["PPE"] = extract_value(pdf_text, "PPE")

        except Exception as e:
            st.error(f"Error during PDF extraction: {e}")

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        mdvp_fo = st.text_input("MDVP:Fo(Hz)", value=extracted_values["MDVP:Fo(Hz)"])

    with col2:
        mdvp_fhi = st.text_input("MDVP:Fhi(Hz)", value=extracted_values["MDVP:Fhi(Hz)"])

    with col3:
        mdvp_flo = st.text_input("MDVP:Flo(Hz)", value=extracted_values["MDVP:Flo(Hz)"])

    # Add input fields for the remaining features
    with col1:
        mdvp_jitter_percent = st.text_input("MDVP:Jitter(%)", value=extracted_values["MDVP:Jitter(%)"])

    with col2:
        mdvp_jitter_abs = st.text_input("MDVP:Jitter(Abs)", value=extracted_values["MDVP:Jitter(Abs)"])

    with col3:
        mdvp_rap = st.text_input("MDVP:RAP", value=extracted_values["MDVP:RAP"])

    # Add input fields for the remaining features
    with col1:
        mdvp_ppq = st.text_input("MDVP:PPQ", value=extracted_values["MDVP:PPQ"])

    with col2:
        jitter_ddp = st.text_input("Jitter:DDP", value=extracted_values["Jitter:DDP"])

    with col3:
        mdvp_shimmer = st.text_input("MDVP:Shimmer", value=extracted_values["MDVP:Shimmer"])

    # Continue adding input fields for the remaining features
    with col1:
        mdvp_shimmer_db = st.text_input("MDVP:Shimmer(dB)", value=extracted_values["MDVP:Shimmer(dB)"])

    with col2:
        shimmer_apq3 = st.text_input("Shimmer:APQ3", value=extracted_values["Shimmer:APQ3"])

    with col3:
        shimmer_apq5 = st.text_input("Shimmer:APQ5", value=extracted_values["Shimmer:APQ5"])
        
    with col1:
        mdvp_apq = st.text_input("MDVP:APQ", value=extracted_values["MDVP:APQ"])

    with col2:
        shimmer_dda = st.text_input("Shimmer:DDA", value=extracted_values["Shimmer:DDA"])

    with col3:
        nhr = st.text_input("NHR", value=extracted_values["NHR"])

    # Continue adding input fields for the remaining features
    with col1:
        hnr = st.text_input("HNR", value=extracted_values["HNR"])

    with col2:
        rpde = st.text_input("RPDE", value=extracted_values["RPDE"])

    with col3:
        dfa = st.text_input("DFA", value=extracted_values["DFA"])

    # Continue adding input fields for the remaining features
    with col1:
        spread1 = st.text_input("spread1", value=extracted_values["spread1"])

    with col2:
        spread2 = st.text_input("spread2", value=extracted_values["spread2"])

    with col3:
        d2 = st.text_input("D2", value=extracted_values["D2"])

    # Continue adding input fields for the remaining features
    with col1:
        ppe = st.text_input("PPE", value=extracted_values["PPE"])


    # Code for Prediction
    parkinsons_diagnosis = ""

    if st.button('Parkinsons Test Result'):
        parkinson_prediction = parkinsons_model.predict([[extracted_values["MDVP:Fo(Hz)"],
                                                          extracted_values["MDVP:Fhi(Hz)"],
                                                          extracted_values["MDVP:Flo(Hz)"],
                                                          extracted_values["MDVP:Jitter(%)"],
                                                          extracted_values["MDVP:Jitter(Abs)"],
                                                          extracted_values["MDVP:RAP"],
                                                          extracted_values["MDVP:PPQ"],
                                                          extracted_values["Jitter:DDP"],
                                                          extracted_values["MDVP:Shimmer"],
                                                          extracted_values["MDVP:Shimmer(dB)"],
                                                          extracted_values["Shimmer:APQ3"],
                                                          extracted_values["Shimmer:APQ5"],
                                                          extracted_values["MDVP:APQ"],
                                                          extracted_values["Shimmer:DDA"],
                                                          extracted_values["NHR"],
                                                          extracted_values["HNR"],
                                                          extracted_values["RPDE"],
                                                          extracted_values["DFA"],
                                                          extracted_values["spread1"],
                                                          extracted_values["spread2"],
                                                          extracted_values["D2"],
                                                          extracted_values["PPE"]]])
                                                      
                        

        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = 'The person has Parkinsons disease'
        else:
            parkinson_diagnosis = 'The person does not have Parkinsons disease'

    st.success(parkinsons_diagnosis)
