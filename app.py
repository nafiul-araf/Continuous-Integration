# area calculator

# area of a circle
# area of a ractangle
# area of triangle
import math
import streamlit as st

st.title("Area Calculator")
st.write("This calculator has been created for calculating the area of a circle/triangle/ractangle")

options = ["circle", "triangle", "ractangle"]
selected_option = st.selectbox("Select an Option", options)

if selected_option == "circle":
    st.write("You selected:", selected_option)
    radius = st.number_input("Enter the radius of the circle", value=0.0, step=0.1)
    circ_area = round(math.pi * radius ** 2, 2)
    st.write(f"The area of the circle for radius={radius} is: {circ_area}")

elif selected_option == "triangle":
    st.write("You selected:", selected_option)
    base = st.number_input("Enter the base of the triangle", value=0.0, step=0.1)
    height = st.number_input("Enter the height of the triangle", value=0.0, step=0.1)
    triangle_area = round(0.5 * base * height, 2)
    st.write(f"The area of the triangle for base={base} and height={height} is: {triangle_area}")

else:
    st.write("You selected:", selected_option)
    length = st.number_input("Enter the length of the ractangle", value=0.0, step=0.1)
    width = st.number_input("Enter the width of the ractangle", value=0.0, step=0.1)
    ractangle_area = round(length * width, 2)
    st.write(f"The area of the triangle for length={length} and width={width} is: {ractangle_area}")