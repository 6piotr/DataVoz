
from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_BD = BASE_DIR / "data" / "datavoz.db"


def conectar():
    conexion = sqlite3.connect(RUTA_BD)
    return conexion
