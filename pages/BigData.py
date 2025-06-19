import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análisis Big Data",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Panel de Análisis Exploratorio de Datos")
st.markdown("---")

if 'data' not in st.session_state:
    st.error("⚠️ No se han cargado datos para analizar")
    st.link_button("⬅️ Volver a la página de carga", "1-🏠Inicio.py")
    st.stop()

data = st.session_state['data']

with st.expander("🔍 Ver información del dataset"):
    st.write(f"**Filas:** {data.shape[0]}, **Columnas:** {data.shape[1]}")
    st.dataframe(data.head(3))

columnas_numericas = data.select_dtypes(include=['number']).columns.tolist()
columnas_texto = data.select_dtypes(include=['object', 'category', 'string']).columns.tolist()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📦 Diagrama de Caja", 
    "🟡 Dispersión", 
    "📊 Barras", 
    "📈 Líneas", 
    "🧮 Histograma"
])

with tab1:
    st.header("Diagrama de Caja y Bigotes")
    if columnas_numericas and columnas_texto:
        x_col = st.selectbox("Variable categórica (eje X):", columnas_texto)
        y_col = st.selectbox("Variable numérica (eje Y):", columnas_numericas)
        fig = px.box(data, x=x_col, y=y_col)
        st.plotly_chart(fig)
    else:
        st.warning("Se requieren columnas categóricas y numéricas.")

with tab2:
    st.header("Gráfico de Dispersión")
    if len(columnas_numericas) >= 2:
        x_col = st.selectbox("Columna eje X:", columnas_numericas)
        y_col = st.selectbox("Columna eje Y:", columnas_numericas, index=1)
        fig = px.scatter(data, x=x_col, y=y_col)
        st.plotly_chart(fig)
    else:
        st.warning("Se necesitan al menos dos columnas numéricas para el gráfico de dispersión.")

with tab3:
    st.header("Gráfico de Barras")
    if columnas_texto and columnas_numericas:
        cat_col = st.selectbox("Categoría:", columnas_texto)
        val_col = st.selectbox("Valor:", columnas_numericas)
        fig = px.bar(data, x=cat_col, y=val_col)
        st.plotly_chart(fig)
    else:
        st.warning("Se necesitan columnas categóricas y numéricas para el gráfico de barras.")

with tab4:
    st.header("Gráfico de Líneas")
    if len(columnas_numericas) >= 2:
        x_col = st.selectbox("Eje X:", columnas_numericas)
        y_col = st.selectbox("Eje Y:", columnas_numericas, index=1)
        fig = px.line(data, x=x_col, y=y_col)
        st.plotly_chart(fig)
    else:
        st.warning("Se requieren al menos dos columnas numéricas.")

with tab5:
    st.header("Histograma")
    if columnas_numericas:
        col = st.selectbox("Columna:", columnas_numericas)
        fig = px.histogram(data, x=col)
        st.plotly_chart(fig)
    else:
        st.warning("No hay columnas numéricas disponibles para el histograma.")