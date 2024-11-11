import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from joblib import dump
import joblib
# from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import streamlit as st
model = joblib.load('model.joblib')
# Load your data
# from sklearn.datasets import fetch_california_housing
with st.form("my_form"):
    uploaded_file = st.file_uploader("Choose a CSV file")
    submitted=st.form_submit_button()
    if submitted:
    # To read the CSV file as a pandas DataFrame:

        df = pd.read_csv(uploaded_file)
        X_test=df.drop('Target',axis=1)
        y_test=df['Target']
        # st.write(X_test.shape,df.shape)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        st.write("Mean Squared Error:", mse)

# st.write("Mean Squared Error:")

# california_housing = fetch_california_housing()

# df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)
# df['Target'] = california_housing.target

# X = df.drop('Target', axis=1)
# # X.shape
# y=df['Target']
# Preprocess data (if needed)
# Standard Scaling

# Initialize and apply StandardScaler
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# Split data into features and target


# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Create and train the model
# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# mse = mean_squared_error(y_test, y_pred)
# print("Mean Squared Error:", mse) 
# print(pd.concat([pd.DataFrame(X_test),pd.DataFrame(y_test)]).to_csv(r'D:\\MLOps\docker_learn\\testing.csv'))
# Save the model
# import os 
# os.chdir(r'D:\\MLOps\docker_learn')

