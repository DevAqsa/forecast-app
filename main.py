import streamlit as st
import plotly.express as px
from backend import get_data

# add title , text input , slider , selectbox, and subheader
st.title("Weather Forecast for the next Days")
place = st.text_input("Enter a place to forecast")
days = st.slider("Forecast days", min_value=1, max_value=5, help="selected the numbers of the forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # get the temperature/sky data
    try:
        filtered_data= get_data(place, days)

        if option == "Temperature":
            Temperature = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # create the temperature plot
            figure = px.line(x=dates, y=Temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=200)

    except KeyError:
        st.write("No data available")