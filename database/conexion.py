
import sqlite3


def conectar():
    conexion = sqlite3.connect("data/datavoz.db")
    return conexion
