import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the next Days")
place = st.text_input("Enter a place to forecast")
days = st.slider("Forecast days", min_value=1, max_value=5, help="selected the numbers of the forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "sky"))

st.subheader(f"{option} for the next {days} days in {place}")

figure = px.line()

st.plotly_chart()