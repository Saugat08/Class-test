%%writefile app.py
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'trained_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a Streamlit app
st.title("Monthly Revenue Prediction")

# Add input fields for the features
st.sidebar.header("Input Features")
total_customers = st.sidebar.number_input("Total Customers", min_value=0)
average_order_value = st.sidebar.number_input("Average Order Value", min_value=0.0)
customer_acquisition_cost = st.sidebar.number_input("Customer Acquisition Cost", min_value=0.0)
marketing_spend = st.sidebar.number_input("Marketing Spend", min_value=0.0)
website_traffic = st.sidebar.number_input("Website Traffic", min_value=0)
conversion_rate = st.sidebar.number_input("Conversion Rate", min_value=0.0, max_value=1.0)
average_order_frequency = st.sidebar.number_input("Average Order Frequency", min_value=0.0)

# Create a button to predict
if st.sidebar.button("Predict Revenue"):
    # Prepare the input data as a DataFrame
    input_data = pd.DataFrame({
        'total_customers': [total_customers],
        'average_order_value': [average_order_value],
        'customer_acquisition_cost': [customer_acquisition_cost],
        'marketing_spend': [marketing_spend],
        'website_traffic': [website_traffic],
        'conversion_rate': [conversion_rate],
        'average_order_frequency': [average_order_frequency]
    })

    # Make the prediction using the loaded model
    predicted_revenue = loaded_model.predict(input_data)[0]

    # Display the prediction
    st.subheader("Predicted Monthly Revenue:")
    st.write(f"${predicted_revenue:.2f}")
