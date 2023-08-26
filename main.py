import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("My Best Company!")

text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
st.write(text)

st.header("Our Team")

col1, emp_col1, col2, emp_col2, col3 = st.columns([4, 1, 4, 1, 4])

df = pd.read_csv("data.csv")
with col1:
    for index, row in df[:4].iterrows():
        st.header(row['first name'].title() + " " + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'])

with col2:
    for index, row in df[5:9].iterrows():
        st.header(row['first name'].title() + " " + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'])

with col3:
    for index, row in df[9:].iterrows():
        st.header(row['first name'].title() + " " + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'])


