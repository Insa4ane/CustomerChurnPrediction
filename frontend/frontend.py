import streamlit as st
import requests as rq
from scripts.DataLoader import DataLoader


class Frontend:
    def __init__(self, columns):
        self.columns = columns

    def main_menu(self):
        st.title("Prognoza odejsc klientow")
        st.header("Podaj dane klienta ")
        written_data={}
        with st.form(key="Miejsce na wpisanie danych"):
            st.subheader("Podaj dane klienta ")
            for column in self.columns:
                response=st.text_input(f"Write below {column}")
                written_data[column]=response
            create_form=st.form_submit_button(label="Send")
        return create_form


    def run(self):
        create_form=self.main_menu()










