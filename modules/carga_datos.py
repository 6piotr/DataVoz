
import pandas as pd
from modules.validacion import validar_encuestas
from modules.guardar_datos import guardar_encuestas


def cargar_encuestas(ruta):
    datos = pd.read_csv(ruta)
    return datos


if __name__ == "__main__":

    datos = cargar_encuestas("data/encuestas.csv")

    errores = validar_encuestas(datos)

    print("Total de encuestas:", len(datos))

    if errores:
        print("\nProblemas encontrados:")

        for error in errores:
            print("-", error)

    else:
        print("\nNo se encontraron problemas.")

        guardar_encuestas(datos)
