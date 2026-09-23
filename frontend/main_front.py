import streamlit as st
from config.config import COLUMNS_TYPES
from ui import Frontend
import joblib

def main_menu():
    st.title("Strona do przewidywania")
    columns_with_types = joblib.load(COLUMNS_TYPES)
    frontend = Frontend(columns_with_types)
    create_form, written_data=frontend.main_menu()
    if create_form and written_data:
        response = frontend.send_data(create_form, written_data)
        if response is not None and response.status_code == 200:
            result = response.json()["result"]
            if result == "Yes":
                st.success("Klient najprawdopodobniej zrezygnuje z usługi.")
            else:
                st.success("Klient najprawdopodobniej pozostanie z nami.")
        else:
            st.error(f"Błąd zapytania: {response}")


if __name__ == "__main__":
    main_menu()

