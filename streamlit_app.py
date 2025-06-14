# streamlit_app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Page title
st.title("Employee Attrition Dashboard")

# Load your dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/employee.csv")

df = load_data()
st.write("### Dataset Preview", df.head())

df['salary'] = df['salary'].map({'low':0, 'medium':1, 'high':2})

# Sidebar: select feature to explore against attrition
feature = st.selectbox(
    "Select a feature to compare against employee attrition:",
    ["satisfaction_level", "time_spend_company", "Work_accident", "salary"]
)

# Map 'left' to more human-readable labels
df["left_label"] = df["left"].map({0: "Stayed", 1: "Left"})

fig = px.histogram(data_frame=df, 
                   x=feature,
                   color='left_label',
                   title=f"Distribution of {feature.replace('_', ' ').capitalize()} by Employee Attrition",
                   labels={feature: feature.replace("_", " ").capitalize()}
                   )

st.plotly_chart(fig, use_container_width=True)