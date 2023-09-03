import csv
import pandas as pd

import streamlit as st
from send_email import send_email

st.header("Contact us!")

with st.form(key='email_form', clear_on_submit=True):
    email = st.text_input("Your Email here")

    # creating option for select box using pandas
    df = pd.read_csv("C:/Users/shrav/PycharmProjects/Portfolio/studentproject1/topics.csv")
    options = [option[0] for option in df.values]

    option_selected = st.selectbox("What topic do you want to discuss?", options)

    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    mail_text = f"""\
Subject: New mail from {email} for {option_selected}

From: {email}
{message} 
"""

if button:
    send_email(mail_text)
    st.info("Your Email sent")