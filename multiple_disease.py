# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:44:15 2022

@author: Sobhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the models

diabetes = pickle.load(open("diabetes_model.sav", "rb"))

heart_disease = pickle.load(open("heart_disease_model.sav", "rb"))

parkinsons_disease = pickle.load(open("parkinsons_disease_model.sav", "rb"))

breast_cancer = pickle.load(open("breast_cancer_model.sav", "rb"))

lung_cancer = pickle.load(open("lung_cancer_model.sav", "rb"))


#sidebar for navigation

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System using Machine Learning", 
                           
                           ["Diabetes Prediction",
                            "Heart Disese Prediction",
                            "Parkinsons Disease Prediction",
                            "Breast Cancer Prediction",
                            "Lung Cancer Prediction"],
                           
                           icons = ["activity", "heart-fill", "people-fill", 
                                    "gender-female", "apple"],
                           
                           default_index = 0)








#Diabetes Prediction Page:

if(selected == "Diabetes Prediction"):
    
    #page title
    st.title("Diabetes Prediction using Machine Learning")
    
    

# getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        
    with col2:
        Glucose = st.text_input("Glucose Level")
    
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    
    with col2:
        Insulin = st.text_input("Insulin Level")
    
    with col3:
        BMI = st.text_input("BMI Value")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    
    with col2:
        Age = st.text_input("Age of the Person")


# code for Prediction
    diabetes_diagnosis = " "
    
    # creating a button for Prediction
    
    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diabetes_prediction[0] == 0):
          diabetes_diagnosis = "Hurrah! You have no Diabetes."
        else:
          diabetes_diagnosis = "Sorry! You have Diabetes."
        
    st.success(diabetes_diagnosis)



















#Heart Disease Prediction Page:

if(selected == "Heart Disese Prediction"):
    
    #page title
    st.title("Heart Disease Prediction using Machine Learning")
    
    
    
# getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age")
        
    with col2:
        sex = st.number_input("Sex")
        
    with col3:
        cp = st.number_input("Chest Pain Types")
        
    with col1:
        trestbps = st.number_input("Resting Blood Pressure")
        
    with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl")
        
    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl")
        
    with col1:
        restecg = st.number_input("Resting Electrocardiographic Results")
        
    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved")
        
    with col3:
        exang = st.number_input("Exercise Induced Angina")
        
    with col1:
        oldpeak = st.number_input("ST Depression induced by Exercise")
        
    with col2:
        slope = st.number_input("Slope of the peak exercise ST Segment")
        
    with col3:
        ca = st.number_input("Major vessels colored by Flourosopy")
        
    with col1:
        thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
        
        
     
     
    # code for Prediction
    heart_diagnosis = " "
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 0):
          heart_diagnosis = "Hurrah! Your Heart is Good."
        else:
          heart_diagnosis = "Sorry! You have Heart Problem."
        
    st.success(heart_diagnosis)
        











#Parkinsons Disease Prediction Page:

if(selected == "Parkinsons Disease Prediction"):
    
    #page title
    st.title("Parkinsons Disease Prediction using Machine Learning")



# getting the input data from the user

    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
        
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
        
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
        
    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
        
    with col1:
        RAP = st.text_input("MDVP:RAP")
        
    with col2:
        PPQ = st.text_input("MDVP:PPQ")
        
    with col3:
        DDP = st.text_input("Jitter:DDP")
        
    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")
        
    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
        
    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")
        
    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")
        
    with col3:
        APQ = st.text_input("MDVP:APQ")
        
    with col4:
        DDA = st.text_input("Shimmer:DDA")
        
    with col5:
        NHR = st.text_input("NHR")
        
    with col1:
        HNR = st.text_input("HNR")
        
    with col2:
        RPDE = st.text_input("RPDE")
        
    with col3:
        DFA = st.text_input("DFA")
        
    with col4:
        spread1 = st.text_input("spread1")
        
    with col5:
        spread2 = st.text_input("spread2")
        
    with col1:
        D2 = st.text_input("D2")
        
    with col2:
        PPE = st.text_input("PPE")
        
    
    
    # code for Prediction
    parkinsons_diagnosis = " "
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_disease.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 0):
          parkinsons_diagnosis = "Hurrah! You don't have Parkinson's Disease."
        else:
          parkinsons_diagnosis = "Sorry! You have Parkinson's Disease."
        
    st.success(parkinsons_diagnosis)  
















#Breast Cancer Prediction Page:

if(selected == "Breast Cancer Prediction"):
    
    #page title
    st.title("Breast Cancer Prediction using Machine Learning")



# getting the input data from the user

    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        id = st.number_input("id")
    
    with col2:
        radius_mean = st.number_input("radius_mean")
        
    with col3:
        texture_mean = st.number_input("texture_mean")
        
    with col4:
        perimeter_mean = st.number_input("perimeter_mean")
        
    with col5:
        area_mean = st.number_input("area_mean")
        
    with col1:
        smoothness_mean = st.number_input("smoothness_mean")
        
    with col2:
        compactness_mean = st.number_input("compactness_mean")
        
    with col3:
        concavity_mean= st.number_input("concavity_mean")
        
    with col4:
        concave_points_mean = st.number_input("concave points_mean")
        
    with col5:
        symmetry_mean = st.number_input("symmetry_mean")
        
    with col1:
        fractal_dimension_mean = st.number_input("fractal_dimension_mean")
        
    with col2:
       radius_se = st.number_input("radius_se")
        
    with col3:
        texture_se = st.number_input("texture_se")
        
    with col4:
        perimeter_se = st.number_input("perimeter_se")
        
    with col5:
        area_se = st.number_input("area_se")
        
    with col1:
       smoothness_se = st.number_input("smoothness_se")
        
    with col2:
       compactness_se = st.number_input("compactness_se")
        
    with col3:
        concavity_se = st.number_input("concavity_se")
        
    with col4:
       concave_points_se = st.number_input("concave points_se")
        
    with col5:
        symmetry_se = st.number_input("ssymmetry_se")
        
    with col1:
        fractal_dimension_se = st.number_input("fractal_dimension_se")
        
    with col2:
       radius_worst = st.number_input("radius_worst")
        
    with col3:
        texture_worst = st.number_input("texture_worst")
    
    with col4:
        perimeter_worst = st.number_input("perimeter_worst")
        
    with col5:
       area_worst = st.number_input("area_worst")
        
    with col1:
        smoothness_worst = st.number_input("smoothness_worst")
        
    with col2:
        compactness_worst = st.number_input("compactness_worst")
        
    with col3:
        concavity_worst = st.number_input("concavity_worst")
        
    with col4:
        concave_points_worst = st.number_input("concave points_worst")
        
    with col5:
        symmetry_worst = st.number_input("symmetry_worst")
    
    with col1:
        fractal_dimension_worst = st.number_input("fractal_dimension_worst")
        
    
    #code for Prediction
    breast_cancer_check = " "

    if st.button("Breast Cancer Test Result"):
        breast_cancer_prediction = breast_cancer.predict([[id, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])                          
   
        if (breast_cancer_prediction[0] == 0):
        
           breast_cancer_check = "Hurrah! You don't have Breast Cancer."
        else:
         breast_cancer_check = "Sorry! You have Breast Cancer."

    st.success(breast_cancer_check) 
      











#Lung Cancer Prediction Page:

if(selected == "Lung Cancer Prediction"):
    
    #page title
    st.title("Lung Cancer Prediction using Machine Learning")



# getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        GENDER = st.number_input("GENDER")
        
    with col2:
        AGE = st.number_input("AGE")
    
    with col3:
        SMOKING = st.number_input("SMOKING")
    
    with col4:
        YELLOW_FINGERS = st.number_input("YELLOW_FINGERS")
    
    with col1:
        ANXIETY = st.number_input("ANXIETY")
    
    with col2:
        PEER_PRESSURE = st.number_input("PEER_PRESSURE")
    
    with col3:
        CHRONIC_DISEASE = st.number_input("CHRONIC DISEASE")
    
    with col4:
        FATIGUE = st.number_input("FATIGUE")
    
    with col1:
        ALLERGY = st.number_input("ALLERGY")
    
    with col2:
        WHEEZING = st.number_input("WHEEZING")
    
    with col3:
        ALCOHOL_CONSUMING = st.number_input("ALCOHOL CONSUMING")
    
    with col4:
        COUGHING = st.number_input("COUGHING")
    
    with col1:
        SHORTNESS_OF_BREATH = st.number_input("SHORTNESS OF BREATH")
    
    with col2:
        SWALLOWING_DIFFICULTY = st.number_input("SWALLOWING DIFFICULTY")
    
    with col3:
        CHEST_PAIN = st.number_input("CHEST PAIN")
    


# code for Prediction
    lung_cancer_result = " "
    
    # creating a button for Prediction
    
    if st.button("Lung Cancer Test Result"):
        lung_cancer_report = lung_cancer.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        
        if (lung_cancer_report[0] == 0):
          lung_cancer_result = "Hurrah! You have no Lung Cancer."
        else:
          lung_cancer_result = "Sorry! You have Lung Cancer."
        
    st.success(lung_cancer_result)
 


