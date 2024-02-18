import streamlit as st
import pandas as pd

def data():
    st.title('Data Page')
    
    # Connect to the database and fetch sample data
    df = pd.read_csv('cleaned_data.csv')

    # Display cleaned data
    st.write('Cleaned Data:')
    st.dataframe(df.head())

    # Users to view numeric features
    numeric_features = df.select_dtypes(include=['float64', 'int64'])
    st.write('Numeric Features:')
    st.write(numeric_features.columns.tolist())

    # Users to view categorical features
    categorical_features = df.select_dtypes(include=['object'])
    st.write('Categorical Features:')
    st.write(categorical_features.columns.tolist())

# Call the data function directly
if __name__ == '__main__':
    data()
