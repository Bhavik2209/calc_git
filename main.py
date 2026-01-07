from operations import addition
import streamlit as st

# from operations.addition import add
# from operations.subtraction import subtract
# from operations.multiplication import multiply
# from operations.division import divide

st.title("Modular Calculator")

# Using Session State to store values
if "calc_display" not in st.session_state:
    st.session_state.calc_display = ""

# Layout for UI
col1, col2 = st.columns(2)
num1 = col1.number_input("First Number", value=0.0)
num2 = col2.number_input("Second Number", value=0.0)

st.write("### Choose Operation")
c1, c2, c3, c4 = st.columns(4)

result = 0.0

if c1.button("+"):
    result = add(num1, num2)
    st.success(f"Result: {result}")

if c2.button("-"):
    result = subtract(num1, num2)
    st.success(f"Result: {result}")

if c3.button("×"):
    result = multiply(num1, num2)
    st.success(f"Result: {result}")

if c4.button("÷"):
    if num2 != 0:
        result = divide(num1, num2)
        st.success(f"Result: {result}")
    else:
        st.error("Cannot divide by zero!")