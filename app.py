# app.py
import streamlit as st
import pandas as pd
from io import StringIO
import os
from PIL import Image 

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Gestión Mundo Autos",
    layout="wide",
    page_icon="📊"
)

def main():
    # Header con estilo
    st.title("📊 Sistema de Gestión Mundo Autos 🚘🚗")
    st.markdown("---")

    # Sección de bienvenida
    col1, col2 = st.columns([3, 2])

    with col1:
        st.header("Bienvenido pip pip")
        st.write("""
        Este sistema te permite:
        - Visualizar un archivo csv de autos
        - Visualizar y explorar los multiples tipos de datos
        - Generar prediccion de gustos por medio de entrada de datos
        - Exportar resultados
        """)
        st.info("💡 Comienza Visualizando el archivo y su información en el menu de inicio")

    with col2:
        st.image(
            "https://storage.googleapis.com/kaggle-datasets-images/7602891/12077823/9b881ee02a7344e73799487da10f6101/dataset-cover.jpg?t=2025-06-06-08-27-15",
            caption=""
        )

if __name__ == "__main__":
    main()

# Pie de página
st.markdown("---")
st.caption("Panel desarrollado con Streamlit y Plotly | © 2025 Análisis Big Data")