import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
import streamlit as st

model = joblib.load('model.joblib')

def process_upload(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        X_test = df.drop('Target', axis=1)
        y_test = df['Target']
        
        # Prediction
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        return mse, df.shape  # Return MSE and shape for testing
    
    else:
        raise ValueError("No file uploaded")

def main():
    with st.form("my_form"):
        uploaded_file = st.file_uploader("Choose a CSV file")
        submitted = st.form_submit_button("Submit")
        
        if submitted and uploaded_file:
            mse, shape = process_upload(uploaded_file)
            st.write("Mean Squared Error:", mse)
            st.write("Dataframe shape:", shape)
