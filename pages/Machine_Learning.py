import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Predicción de Región", page_icon="🌍", layout="wide")

st.title("🌍 Predicción de Región de Venta del Auto")
st.markdown("---")

# Validar si hay datos cargados
if 'data' not in st.session_state:
    st.warning("No se han cargado datos desde la página de inicio.")
    st.stop()

data = st.session_state['data'].copy()

# Preprocesamiento: limpiar columnas de precios (remover "$", "," y espacios)
def limpiar_precio(col):
    return data[col].replace('[\$, ]', '', regex=True).astype(float)

data['MSRP'] = limpiar_precio('MSRP')
data['DealerCost'] = limpiar_precio('DealerCost')

# Codificar etiquetas
label_encoder = LabelEncoder()
data = data.dropna(subset=['Region'])  # Eliminar nulos
data['Region_encoded'] = label_encoder.fit_transform(data['Region'])

# Variables independientes y target
features = ['MSRP', 'DealerCost', 'EngineSize', 'Cylinders', 'HorsePower',
            'MPG_City', 'MPG_Highway', 'Weight', 'Wheelbase', 'Length']

# Diccionario con etiquetas en español para cada feature
etiquetas_es = {
    'MSRP': 'Precio MSRP (Precio de Venta Sugerido por el Fabricante)',
    'DealerCost': 'Costo del Dealer',
    'EngineSize': 'Tamaño del Motor',
    'Cylinders': 'Cilindros',
    'HorsePower': 'Caballos de Fuerza',
    'MPG_City': 'Millas por Galón en Ciudad',
    'MPG_Highway': 'Millas por Galón en Carretera',
    'Weight': 'Peso',
    'Wheelbase': 'Distancia entre Ejes',
    'Length': 'Longitud'
}

X = data[features]
y = data['Region_encoded']

# Entrenar el modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42, test_size=0.3)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Mostrar precisión del modelo
st.write(f"**Precisión del modelo:** {model.score(X_test, y_test)*100:.2f}%")

# Ingreso de datos por el usuario
st.subheader("1. Ingrese los datos del vehículo")

user_input = {}
for feature in features:
    min_val = float(X[feature].min())
    max_val = float(X[feature].max())
    default_val = float(X[feature].mean())
    user_input[feature] = st.number_input(
        etiquetas_es[feature], min_value=min_val, max_value=max_val, value=default_val
    )

input_df = pd.DataFrame([user_input])

# Predecir la región
if st.button("Predecir Región"):
    proba = model.predict_proba(input_df)[0]
    top_3_idx = np.argsort(proba)[::-1][:5]
    top_3_regions = label_encoder.inverse_transform(top_3_idx)
    top_3_probs = proba[top_3_idx]

    st.success(f"La región más probable es: **{top_3_regions[0]}**")

    fig, ax = plt.subplots()
    sns.barplot(x=top_3_probs, y=top_3_regions, ax=ax, palette="viridis")
    ax.set_xlabel("Probabilidad")
    ax.set_title("Top 3 Regiones más Probables")
    st.pyplot(fig)
