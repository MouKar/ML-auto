import pandas as pd

import joblib
from app import process_upload
from sklearn.metrics import mean_squared_error
import streamlit as st
# model = joblib.load('model.joblib')
# def process_upload(file_csv):
    
#     with st.form("my_form"):
#         uploaded_file = st.file_uploader("Choose a CSV file")
#         submitted=st.form_submit_button()
submitted=process_upload(file_csv))
if submitted:
    # To read the CSV file as a pandas DataFrame:

    df = pd.read_csv(uploaded_file)
    X_test=df.drop('Target',axis=1)
    y_test=df['Target']
    # st.write(X_test.shape,df.shape)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    st.write("Mean Squared Error:", mse)

