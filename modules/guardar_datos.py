from database.conexion import conectar


def guardar_encuestas(datos):

    conexion = conectar()

    existentes = conexion.execute(
        """
        SELECT region, edad, preferencia_politica,
               intencion_voto, fuente
        FROM encuestas
        """
    ).fetchall()

    columnas = [
        "region",
        "edad",
        "preferencia_politica",
        "intencion_voto",
        "fuente"
    ]

    registros_existentes = set(existentes)

    datos_nuevos = datos[
        ~datos[columnas].apply(tuple, axis=1).isin(registros_existentes)
    ]

    if not datos_nuevos.empty:
        datos_nuevos.to_sql(
            "encuestas",
            conexion,
            if_exists="append",
            index=False
        )

    print("Registros nuevos guardados:", len(datos_nuevos))

    conexion.close()