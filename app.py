
import streamlit as st
import plotly.express as px
from database.inicializar import inicializar_base_datos

from modules.analisis import (
    obtener_encuestas,
    analizar_por_region,
    analizar_por_edad,
    analizar_por_preferencia,
    analizar_por_voto
)


st.set_page_config(
    page_title="DataVoz",
    page_icon="📊",
    layout="wide"
)


st.title("DataVoz | Sistema de análisis")
st.write("Plataforma de análisis de encuestas.")

# Preparar la base de datos antes de consultar
try:
    inicializar_base_datos()
    datos = obtener_encuestas()

except Exception as error:
    st.error(f"No se pudo iniciar DataVoz: {error}")
    st.stop()


# Filtros del dashboard
st.sidebar.header("Filtros")

regiones = ["Todas"] + sorted(datos["region"].unique().tolist())

region_seleccionada = st.sidebar.selectbox(
    "Seleccionar región",
    regiones
)

edad_minima = int(datos["edad"].min())
edad_maxima = int(datos["edad"].max())

rango_edad = st.sidebar.slider(
    "Rango de edad",
    min_value=edad_minima,
    max_value=edad_maxima,
    value=(edad_minima, edad_maxima)
)


# Aplicar filtros
datos_filtrados = datos.copy()

if region_seleccionada != "Todas":
    datos_filtrados = datos_filtrados[
        datos_filtrados["region"] == region_seleccionada
    ]

datos_filtrados = datos_filtrados[
    (datos_filtrados["edad"] >= rango_edad[0]) &
    (datos_filtrados["edad"] <= rango_edad[1])
]


# Comprobar si existen resultados
if datos_filtrados.empty:

    st.warning("No hay encuestas para los filtros seleccionados.")

else:

    # Indicadores principales
    col1, col2, col3 = st.columns(3)

    col1.metric("Total de encuestas", len(datos_filtrados))
    col2.metric("Edad promedio", round(datos_filtrados["edad"].mean(), 1))
    col3.metric("Regiones", datos_filtrados["region"].nunique())


    st.divider()


    # Encuestas por región
  
    # Encuestas por región
    st.subheader("Encuestas por región")

    region = analizar_por_region(datos_filtrados)

    fig_region = px.bar(
        x=region.index,
        y=region.values,
        labels={"x": "Región", "y": "Encuestas"},
        title="Distribución de encuestas por región"
    )

    st.plotly_chart(fig_region, width="stretch")


    # Estadísticas de edad
    st.subheader("Estadísticas de edad")

    estadisticas = analizar_por_edad(datos_filtrados)

    col1, col2, col3 = st.columns(3)

    col1.metric("Edad mínima", int(estadisticas["min"]))
    col2.metric("Edad máxima", int(estadisticas["max"]))
    col3.metric("Mediana", round(estadisticas["50%"], 1))


    # Preferencia política
    st.subheader("Preferencia política")

    preferencias = analizar_por_preferencia(datos_filtrados)

    fig_preferencias = px.pie(
        names=preferencias.index,
        values=preferencias.values,
        title="Preferencias políticas"
    )

    st.plotly_chart(fig_preferencias, width="stretch")


    # Intención de voto
    st.subheader("Intención de voto")

    votos = analizar_por_voto(datos_filtrados)

    fig_votos = px.bar(
        x=votos.index,
        y=votos.values,
        labels={"x": "Candidato", "y": "Encuestas"},
        title="Distribución de intención de voto"
    )

    st.plotly_chart(fig_votos, width="stretch")
