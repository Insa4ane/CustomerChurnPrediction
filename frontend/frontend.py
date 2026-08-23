import streamlit as st
import requests as rq
from config.config import URL
import pandas as pd

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


    def run(self):
        create_form, written_data=self.main_menu()
        if create_form:
            if  written_data['MonthlyCharges'] is not None and written_data['TotalCharges'] is not None:
                api_adres=self.url
                try:
                    response=rq.post(api_adres, json=written_data) #wysylamy dane jesli damy rade
                    if response.status_code == 200:
                        response_data=response.json()
                        prediction=response_data.get("result")
                        st.subheader("Wynik predykcji:")

                        if prediction == "Yes" or prediction == 1:
                            st.error(f"Model przewiduje ze klient odejdzie, lepiej daj mu jakis kod rabatowy czy cos (Churn: {prediction})")
                        else:
                            st.success(f"Model przewiduje ze klient zostanie hurra!!! (Churn: {prediction})")
                    else:
                        st.warning(f"nie ma bledu ale nie ma odebnrania danych{response.status_code}")
                except Exception as e:
                    st.error(f"We have a problem with sent data {e}")
            else:
                st.warning("musisz wypelnic totalcharges oraz monthlycharges!!!")














