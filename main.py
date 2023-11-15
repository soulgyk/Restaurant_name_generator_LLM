import streamlit as st   # library to build proof of concept application
import langchain_helper

st.title("Restaurant Name Generator")

cusine = st.sidebar.selectbox("Pick a Cusine", ("Indian", "Arabic", "Mexican", "Chinese", "English", "Korean", "Italian"))


if cusine:
    response = langchain_helper.generate_restaurant_name_and_items(cusine)
    st.header(response['restaurant_name']. strip())
    menu_items = response['menu_items'].strip().split(',')
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)


