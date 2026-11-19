
from database.conexion import conectar

print("Archivo crear_tablas.py ejecutado")


def crear_tabla_encuestas():
    print("Ejecutando función crear_tabla_encuestas")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region TEXT NOT NULL,
            edad INTEGER NOT NULL,
            preferencia_politica TEXT,
            intencion_voto TEXT,
            fuente TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()

    print("Tabla creada correctamente")


if __name__ == "__main__":
    print("Bloque principal ejecutado")
    crear_tabla_encuestas()
