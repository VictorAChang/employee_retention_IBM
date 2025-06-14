# streamlit_app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# from sklearn.ensemble import RandomForestClassifier

# Page title
st.title("Employee Attrition Dashboard")

# Load your dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/employee.csv")

df = load_data()
st.write("### Dataset Preview", df.head())

# Sidebar filters
satisfaction = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
salary = st.selectbox("Salary Level", df['salary'].unique())

# Top features - placeholder chart
st.write("### Top 5 Features Predicting Attrition")
# Assume you've trained a model elsewhere and saved importances
# Plot dummy example
features = ['satisfaction_level', 'time_spend_company', 'salary', 'promotion_last_5years', 'average_monthly_hours']
importances = [0.3, 0.25, 0.2, 0.15, 0.1]
fig, ax = plt.subplots()
sns.barplot(x=importances, y=features, ax=ax)
st.pyplot(fig)

# Optional: Add prediction model (e.g., "what-if" input)
