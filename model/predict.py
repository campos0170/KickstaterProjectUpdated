import numpy as np
import pandas as pd
import seaborn as sns
import joblib
import os
#from componenents.callbacks  import feature_list

feature_list = [
    'goal', 'log_goal',
    'category_name', 'subcategory', 'currency',
    'country_displayable_name', 'city', 'month',
    'staff_pick'
]
# Load the trained pipeline

model = joblib.load("model/kickstarter_success_model.pkl")

def predict_success(input_dict):
    """
    Predict the success of a newcomer Kickstarter project
    :param input_dict:
    :return:
    """

    for feature in feature_list:
        if feature not in input_dict:
            raise ValueError(f"Missing {feature} in input")
        # Create DataFrame with a single row
    input_df = pd.DataFrame([input_dict])
    # Predict using the loaded model

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    return prediction, probability