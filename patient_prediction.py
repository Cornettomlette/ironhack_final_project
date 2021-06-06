import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

def load_Scaler_from_file(file_name = 'scaler_med.sav'):
    return joblib.load(open(file_name, 'rb'))
    
scaler = load_Scaler_from_file()

def load_Random_Forest_from_file(file_name = 'Class_4_smote_rf_full_data_class_weights_small+.sav'):
    return joblib.load(open(file_name, 'rb'))
    
random_Forest = load_Random_Forest_from_file()

def give_prediction(patient_array):
    global scaler
    global random_Forest
    scaled_array = scaler.transform(patient_array)
    test = random_Forest.predict(scaled_array)
    return test

