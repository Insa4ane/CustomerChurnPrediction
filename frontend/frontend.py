import streamlit as st
import requests as rq
from config.config import URL

class Frontend:
    def __init__(self, columns):
        self.columns = columns
        self.url=URL

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
        return create_form, written_data


    def run(self):
        create_form, written_data=self.main_menu()
        if create_form:
            if  written_data['MonthlyCharges'] and written_data['TotalCharges']:
                api_adres=self.url
                try:
                    response=rq.post(api_adres, json=written_data) #wysylamy dane jesli damy rade
                    if response.status_code == 200:
                        #tutaj bnedziemy mieli logike co sie stanie jesli damy rade wyslac wszystkie dane
                        st.success("Success everything is okej")
                    else:
                        st.warning(f"nie ma bledu ale nie ma odebnrania danych{response.status_code}")
                except Exception as e:
                    st.error(f"We have a problem with sent data {e}")
            else:
                st.warning("musisz wypelnic totalcharges oraz monthlycharges!!!")














