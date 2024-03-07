#importing the libraries
import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the models
diabetes = pickle.load(open("diabetes_model.pkl", "rb"))

heart_disease = pickle.load(open("heart_disease_model.pkl", "rb"))

parkinsons_disease = pickle.load(open("parkinsons_model.pkl", "rb"))

breast_cancer = pickle.load(open("breast_cancer_model.pkl", "rb"))

lung_cancer = pickle.load(open("lung_cancer_model.pkl", "rb"))