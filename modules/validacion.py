
import pandas as pd


def validar_encuestas(datos):

    errores = []

    # Comprobar que existan las columnas necesarias
    columnas_obligatorias = [
        "region",
        "edad",
        "preferencia_politica",
        "intencion_voto",
        "fuente"
    ]

    columnas_faltantes = [
        columna for columna in columnas_obligatorias
        if columna not in datos.columns
    ]

    if columnas_faltantes:
        errores.append(
            f"Faltan columnas obligatorias: {columnas_faltantes}"
        )
        return errores

    # Revisar campos vacíos
    for campo in columnas_obligatorias:

        if datos[campo].isnull().any():
            errores.append(
                f"Existen valores vacíos en {campo}"
            )

        if datos[campo].astype(str).str.strip().eq("").any():
            errores.append(
                f"Existen campos en blanco en {campo}"
            )

    # Validar categorías permitidas
    valores_permitidos = {
        "preferencia_politica": [
            "Izquierda", "Centro", "Derecha"
        ],
        "intencion_voto": [
            "Candidato A", "Candidato B", "Candidato C"
        ],
        "fuente": [
            "Web", "Telefonica", "SERVEL"
        ],
        "region": [
            "Metropolitana", "Valparaiso", "Los Lagos",
            "Biobio", "Araucania"
        ]
    }

    for campo, valores in valores_permitidos.items():

        valores_actuales = (
            datos[campo].dropna().astype(str).str.strip()
        )

        valores_invalidos = set(valores_actuales) - set(valores)

        if valores_invalidos:
            errores.append(
                f"Existen valores no permitidos en {campo}: "
                f"{valores_invalidos}"
            )

    # Revisar edades
    edades = pd.to_numeric(datos["edad"], errors="coerce")

    if edades.isnull().any():
        errores.append("Existen edades que no son numéricas")

    else:
        if (edades < 18).any():
            errores.append(
                "Existen encuestados menores de 18 años"
            )

        if (edades > 120).any():
            errores.append("Existen edades fuera de rango")

    # Revisar registros duplicados
    if datos.duplicated().any():
        errores.append("Existen registros duplicados")

    return errores
