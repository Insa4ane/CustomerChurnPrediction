import streamlit as st
import requests as rq
from config.config import URL
import pandas as pd
import logging

class Frontend:
    def __init__(self, columns):
        self.columns = columns
        self.url=URL

    def main_menu(self):
        st.title("Prognoza odejsc klientow")
        st.header("Podaj dane klienta ")
        written_data={}
        with st.form(key="Miejsce na wpisanie danych"):
            st.subheader("Podaj dane klienta")
            for column_name, dtype in self.columns.items():
                if pd.api.types.is_numeric_dtype(dtype):
                    response = st.number_input(f"Wpisz wartość dla {column_name}", value=0.0)
                else:
                    response = st.text_input(f"Wpisz tekst dla {column_name}")

                written_data[column_name] = response
            create_form = st.form_submit_button(label="Send")
        return create_form, written_data

    def send_data(self, create_from, written_data):
       try:
           if create_from:
               if not written_data['MonthlyCharges'] and not written_data['TotalCharges']:
                   st.warning("Musisz wypelnic totalCharges oraz MonthlyChargees")
               respone=rq.post(URL, json=written_data)
               return respone
       except Exception as e:
           logging.error(f"Wystapil blad{e}")


















