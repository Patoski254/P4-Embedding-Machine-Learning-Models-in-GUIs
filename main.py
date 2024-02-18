import streamlit as st
import pandas as pd



def home():
    st.title('Vodafone Customer Churn Prediction')
    st.write('Welcome to the Machine Learning Model App for Vodafone Company!')
    st.write('This app allows you to interact with machine learning models.')
    
    # Add links to home page
    st.write('Links:')
    st.markdown('[GitHub](https://github.com/Patoski254)')
    st.markdown('[LinkedIn](https://linkedin.com/in/patrick-moturi)')
    
if __name__ == '__main__':
    home()