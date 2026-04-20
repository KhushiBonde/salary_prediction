import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('random_forest_regressor_model.pkl')

st.title('Salary Prediction App')
st.write('Enter the details to predict the salary.')

# Input fields for features
age = st.slider('Age', 20, 60, 30)

gender_options = {'Male': 1, 'Female': 0}
gender_selection = st.selectbox('Gender', list(gender_options.keys()))
gender = gender_options[gender_selection]

education_options = {
    'Bachelor\'s': 0,
    'Master\'s': 1,
    'PhD': 2
}
education_selection = st.selectbox('Education Level', list(education_options.keys()))
education_level = education_options[education_selection]

job_title = st.number_input('Job Title (Encoded Value)', min_value=0, value=100) # User needs to input encoded value

years_of_experience = st.slider('Years of Experience', 0.0, 30.0, 5.0)

# Create a DataFrame for prediction
input_data = pd.DataFrame([{
    'Age': age,
    'Gender': gender,
    'Education Level': education_level,
    'Job Title': job_title,
    'Years of Experience': years_of_experience
}])

if st.button('Predict Salary'):
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Salary: ${prediction:,.2f}')
