Descripción General

Este proyecto consiste en una aplicación web construida usando Streamlit, que permite a los usuarios ingresar información en un formulario. La aplicación verifica y valida los datos ingresados utilizando Pydantic y luego los almacena en una hoja de cálculo de Google Sheets. La aplicación también tiene la capacidad de verificar si un usuario ya existe en la hoja de cálculo para evitar duplicados.
Características

    Interfaz de Usuario Streamlit: Un formulario web para ingresar datos del usuario (nombre, edad, actividad).
    Validación de Datos con Pydantic: Asegura que los datos ingresados cumplan con los requisitos específicos (tipo de dato y restricciones).
    Integración con Google Sheets: Almacena y recupera datos de una hoja de cálculo de Google Sheets.
    Verificación de Existencia de Usuario: Comprueba si un usuario ya está registrado antes de agregarlo a la hoja de cálculo.

Requisitos

    Python 3.6 o superior
    Bibliotecas: Streamlit, Pydantic, gspread, Google OAuth2
    Una hoja de cálculo de Google Sheets y las credenciales de autenticación de Google API (archivo key.json)

Instalación

    Instalar las dependencias:

    bash

    pip install streamlit pydantic gspread google-auth

    Clonar el repositorio o descargar los archivos del proyecto.

Configuración

    Configura las credenciales de Google Cloud para acceder a Google Sheets. Guarda el archivo de credenciales como key.json.
    En el archivo de código, actualiza SPREADSHEET_ID con el ID de tu hoja de cálculo de Google Sheets.

Uso

Para ejecutar la aplicación, navega al directorio del proyecto y ejecuta:

bash

streamlit run nombre_del_archivo.py

La aplicación se abrirá en el navegador web predeterminado.
Funcionalidades

    Formulario de Entrada: Ingresa el nombre, edad y actividad del usuario.
    Validación: Verifica que los datos ingresados cumplan con los formatos esperados.
    Almacenamiento en Google Sheets: Guarda los datos en la hoja de cálculo designada.
    Verificación de Duplicados: Comprueba si un usuario ya está registrado antes de agregarlo a la base de datos.
