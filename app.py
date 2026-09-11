import streamlit as st

# Page title
st.title(" My Calculator")
st.write("Welcome to my calculator!")

# Get numbers
a = st.number_input("Enter first number", value=0.0)
b = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Select the operation you want to perform:",
    ["+", "-", "*", "/"]
)

# Calculate button
if st.button("Calculate"):

    if operation == "+":
        result = a + b
        st.success(f"Addition: {result}")

    elif operation == "-":
        result = a - b
        st.success(f"Subtraction: {result}")

    elif operation == "*":
        result = a * b
        st.success(f"Multiplication: {result}")

    elif operation == "/":
        if b == 0:
            st.error("Division cannot be performed by zero.")
        else:
            result = a / b
            st.success(f"Division: {result}")

 