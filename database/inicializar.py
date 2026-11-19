
from pathlib import Path

from database.conexion import conectar
from database.crear_tablas import crear_tabla_encuestas
from modules.carga_datos import cargar_encuestas
from modules.validacion import validar_encuestas
from modules.guardar_datos import guardar_encuestas


BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_CSV = BASE_DIR / "data" / "encuestas.csv"


def inicializar_base_datos():

    # Crear la tabla si todavía no existe
    crear_tabla_encuestas()

    conexion = conectar()

    cantidad = conexion.execute(
        "SELECT COUNT(*) FROM encuestas"
    ).fetchone()[0]

    conexion.close()

    # Cargar el CSV solamente si la tabla está vacía
    if cantidad == 0:

        datos = cargar_encuestas(RUTA_CSV)

        errores = validar_encuestas(datos)

        if errores:
            raise ValueError(
                "Error al validar los datos: " + "; ".join(errores)
            )

        guardar_encuestas(datos)
