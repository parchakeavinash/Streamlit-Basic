import streamlit as st
import datetime
import pandas as pd
import numpy as np
import time as t

st.image("avi.png",caption='posing with my own style',width = 300)

#title
st.title("Welcome to Streamlit")

# header
st.header("Machine Learning")

# sub header
st.subheader("Linear Regression")

# information
st.info("Information detailes of a user!")

# error message
st.error("wrong password")

# success message
st.success("Congratulation for promotion!")

# warning message
st.warning("come on time or else you will be punishment!!")

# write function
st.write("Stay in Discipline")
st.write(range(0))

# markdown
st.markdown("# Tech-Wizard")
st.markdown("## Tech-Wizard")
st.markdown("### Tech-Wizard")
st.markdown(":moon:")

# write text
st.text("streamlit is awesome!")
st.caption("Python is easy and powerful language!")

# to display a mathematical equation
st.latex(r'''a+b x^2+c''')


# widget

# checkbox
st.checkbox("Login")

# button
st.button("Sign In")

# radio
selected_language = st.radio("Which is your favorite programming language", ["Python", "Java", "JavaScript", "C++"])

# selectbox

st.selectbox("Select Your Branch first",["AI","DS","ML","CS","CSE","CE","ME","IT"])

# multiselect
st.multiselect("Choose your strength",["I am confident","I have good Communication","I am good Leader","I am good with Technology"])

# slider
st.select_slider("your current semester CGPA",[4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 9.9])

# slider
st.slider("Enter you Roll_number",1,69)

# number_Input
st.number_input("Pick a number ", 0,100)

# text_input
st.text_input('Enter you Name')
st.text_input('Enter you email_address')
st.text_input('Enter you phone number')

# date_Input
d =st.date_input("When's your birthday", datetime.date(2004, 7, 27))
st.write('Your birthday is:', d)

# time input
st.time_input("hey, what's the timing?")

# textarea
st.text_area("Write a short summary about yourself.")

# file upload
st.file_uploader("Upload your Resume Here")

st.color_picker("Pick your favorite color")

# student progress
st.write("Course Completion")
st.progress(90)

# time waitng spinnign
with st.spinner("just wait"):
    t.sleep(1)
st.success('Done!')

# celebration with ballons
st.balloons()
# st.snow()

# slider side bar titlte
st.sidebar.title("Welcome to Tech-Wizard")
st.sidebar.text_input("Mail address")
st.sidebar.text_input("Password")

st.sidebar.button("login")
st.sidebar.radio("Professional Expert",["Student","Working","Others"])

# data visualization
st.title("Bar Chart")
data = pd.DataFrame(np.random.randn(50,2),columns =["x","y"])
st.bar_chart(data)
st.title("Bar Chart")
st.line_chart(data)
st.title("Area Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)