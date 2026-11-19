
import pandas as pd
from modules.validacion import validar_encuestas


def test_encuestas_validas():

    datos = pd.DataFrame({
        "region": ["Metropolitana", "Valparaiso"],
        "edad": [25, 34],
        "preferencia_politica": ["Centro", "Izquierda"],
        "intencion_voto": ["Candidato A", "Candidato B"],
        "fuente": ["Web", "Telefonica"]
    })

    errores = validar_encuestas(datos)

    assert errores == []


def test_detectar_edad_invalida():

    datos = pd.DataFrame({
        "region": ["Metropolitana"],
        "edad": [15],
        "preferencia_politica": ["Centro"],
        "intencion_voto": ["Candidato A"],
        "fuente": ["Web"]
    })

    errores = validar_encuestas(datos)

    assert "Existen encuestados menores de 18 años" in errores


def test_detectar_campos_vacios():

    datos = pd.DataFrame({
        "region": ["Metropolitana"],
        "edad": [25],
        "preferencia_politica": ["Centro"],
        "intencion_voto": ["Candidato A"],
        "fuente": [None]
    })

    errores = validar_encuestas(datos)

    assert "Existen valores vacíos en fuente" in errores


def test_detectar_duplicados():

    datos = pd.DataFrame({
        "region": ["Metropolitana", "Metropolitana"],
        "edad": [25, 25],
        "preferencia_politica": ["Centro", "Centro"],
        "intencion_voto": ["Candidato A", "Candidato A"],
        "fuente": ["Web", "Web"]
    })

    errores = validar_encuestas(datos)

    assert "Existen registros duplicados" in errores

def test_detectar_categoria_invalida():

    datos = pd.DataFrame({
        "region": ["Metropolitana"],
        "edad": [25],
        "preferencia_politica": ["Izquieda"],
        "intencion_voto": ["Candidato A"],
        "fuente": ["Web"]
    })

    errores = validar_encuestas(datos)

    assert any(
        "valores no permitidos en preferencia_politica" in error
        for error in errores
    )
    
    
def test_detectar_region_invalida():

    datos = pd.DataFrame({
        "region": ["Metropolitna"],
        "edad": [25],
        "preferencia_politica": ["Centro"],
        "intencion_voto": ["Candidato A"],
        "fuente": ["Web"]
    })

    errores = validar_encuestas(datos)

    assert any(
        "valores no permitidos en region" in error
        for error in errores
    )