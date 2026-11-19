
from database.conexion import conectar
import pandas as pd


def obtener_encuestas():

    conexion = conectar()

    datos = pd.read_sql_query(
        "SELECT * FROM encuestas",
        conexion
    )

    conexion.close()

    return datos


def analizar_por_region(datos):

    resultado = datos["region"].value_counts()

    return resultado


def analizar_por_edad(datos):

    resultado = datos["edad"].describe()

    return resultado


def analizar_por_preferencia(datos):

    resultado = datos["preferencia_politica"].value_counts()

    return resultado


def analizar_por_voto(datos):

    resultado = datos["intencion_voto"].value_counts()

    return resultado


if __name__ == "__main__":

    datos = obtener_encuestas()

    print("Encuestas por región:")
    print(analizar_por_region(datos))

    print("\nEstadísticas de edad:")
    print(analizar_por_edad(datos))

    print("\nPreferencia política:")
    print(analizar_por_preferencia(datos))

    print("\nIntención de voto:")
    print(analizar_por_voto(datos))
