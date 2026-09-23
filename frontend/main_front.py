import streamlit as st
from config.config import COLUMNS_TYPES
from frontend.frontend import Frontend
import joblib

def main_menu():
    st.title("Strona do przewidywania")
    columns_with_types = joblib.load(COLUMNS_TYPES)
    frontend = Frontend(columns_with_types)
    create_form, written_data=frontend.main_menu()
    if create_form and written_data:
        response=frontend.send_data(create_form, written_data)
        st.success(response)

