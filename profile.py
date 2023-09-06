# Import necessary libraries
import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Create a title for the app
st.title('Exploratory Data Analysis App')

# Create a file uploader for the user to upload their CSV file
uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

# Create a button for the user to click to run the EDA
if st.button('Perform EDA'):

    # Check if a file has been uploaded
    if uploaded_file is not None:

        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Create a pandas-profiling report and display it with streamlit-pandas-profiling
        pr = ProfileReport(df, explorative=True)
        st_profile_report(pr)

    else:
        st.write('Please upload a CSV file.')

else:
    st.write('Click the button to perform EDA.')
