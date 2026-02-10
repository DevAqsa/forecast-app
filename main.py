import streamlit as st
import plotly.express as px
import backend as get_data

st.title("Weather Forecast for the next Days")
place = st.text_input("Enter a place to forecast")
days = st.slider("Forecast days", min_value=1, max_value=5, help="selected the numbers of the forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "sky"))

st.subheader(f"{option} for the next {days} days in {place}")

d, t = get_data(place, days, option)

# def get_data(days):
#     dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
#     temperatures = [10, 11, 15]
#     temperatures = [days * i for i in temperatures]
#     return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})

st.plotly_chart(figure)

