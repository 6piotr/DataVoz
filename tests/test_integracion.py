
import pandas as pd
import sqlite3

from modules.validacion import validar_encuestas


def test_carga_validacion_y_almacenamiento():

    # Crear datos de prueba
    datos = pd.DataFrame({
        "region": ["Metropolitana", "Valparaiso"],
        "edad": [25, 34],
        "preferencia_politica": ["Centro", "Izquierda"],
        "intencion_voto": ["Candidato A", "Candidato B"],
        "fuente": ["Web", "Telefonica"]
    })

    # Validar los datos
    errores = validar_encuestas(datos)

    assert errores == []

    # Crear una base de datos temporal en memoria
    conexion = sqlite3.connect(":memory:")

    # Guardar los datos
    datos.to_sql(
        "encuestas",
        conexion,
        if_exists="append",
        index=False
    )

    # Consultar los registros almacenados
    resultados = pd.read_sql_query(
        "SELECT * FROM encuestas",
        conexion
    )

    # Comprobar que se almacenaron correctamente
    assert len(resultados) == 2

    conexion.close()


def test_datos_invalidos_no_se_guardan():

    datos = pd.DataFrame({
        "region": ["Metropolitana"],
        "edad": [15],
        "preferencia_politica": ["Centro"],
        "intencion_voto": ["Candidato A"],
        "fuente": ["Web"]
    })

    # Validar los datos
    errores = validar_encuestas(datos)

    # Crear base de datos temporal
    conexion = sqlite3.connect(":memory:")

    if not errores:
        datos.to_sql(
            "encuestas",
            conexion,
            if_exists="append",
            index=False
        )

    # Consultar si existen registros
    tablas = pd.read_sql_query(
        "SELECT name FROM sqlite_master WHERE type='table'",
        conexion
    )

    # Comprobar que no se creó la tabla
    assert tablas.empty

    conexion.close()

def test_detectar_columnas_faltantes():

    datos = pd.DataFrame({
        "region": ["Metropolitana"],
        "edad": [25]
    })

    errores = validar_encuestas(datos)

    assert any("Faltan columnas obligatorias" in error for error in errores)


def test_detectar_edad_no_numerica():

    datos = pd.DataFrame({
        "region": ["Metropolitana"],
        "edad": ["veinticinco"],
        "preferencia_politica": ["Centro"],
        "intencion_voto": ["Candidato A"],
        "fuente": ["Web"]
    })

    errores = validar_encuestas(datos)

    assert "Existen edades que no son numéricas" in errores