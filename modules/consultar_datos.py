
from database.conexion import conectar


def consultar_encuestas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM encuestas")

    resultados = cursor.fetchall()

    for encuesta in resultados:
        print(encuesta)

    print("\nTotal de registros:", len(resultados))

    conexion.close()


if __name__ == "__main__":
    consultar_encuestas()
