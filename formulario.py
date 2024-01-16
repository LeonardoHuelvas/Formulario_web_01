import streamlit as st
from pydantic import BaseModel, ValidationError
import gspread
from google.oauth2.service_account import Credentials

# Definición de la clase User
class User(BaseModel):
    name: str
    age: int
    activity: str

# Autenticación con Google Sheets
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("key.json", scopes=scope)
client = gspread.authorize(creds)

# Utiliza el ID de la hoja de cálculo para abrir la hoja específica
SPREADSHEET_ID = '1fIsFll6DGOtUZKl0BoRNyjVrm0TlV-Dav6sMFGPtrdE'
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# Función para verificar si el usuario ya existe
def user_exists(name):
    records = sheet.get_all_records()
    return any(record['Nombre'] == name for record in records if 'Nombre' in record)

# Función para guardar un nuevo usuario
def save_user(user):
    sheet.append_row([user.name, user.age, user.activity])

# Interfaz de usuario en Streamlit
st.title("Formulario de encuesta")

name = st.text_input("Nombre")
age = st.number_input("Edad", min_value=18)
activity = st.text_input("Actividad", max_chars=14)


if st.button('Enviar'):
    if not user_exists(name):
        try:
            user = User(name=name, age=age, activity=activity)
            save_user(user)
            st.success("Usuario registrado con éxito en Google Sheets.")
        except ValidationError as e:
            st.error(f'Error en la validación: {e}')
    else:
        st.error("El usuario ya está registrado.")
