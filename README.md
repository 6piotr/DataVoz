# DataVoz | Sistema de análisis de encuestas

## Descripción

DataVoz es un sistema de análisis de encuestas desarrollado en Python. Su objetivo es cargar, validar, almacenar y analizar información mediante una base de datos SQLite y un dashboard interactivo.

El proyecto utiliza datos ficticios para representar un escenario de análisis de preferencias políticas e intención de voto. Fue desarrollado con fines académicos para integrar conocimientos de programación, bases de datos, análisis de datos y visualización.

## Tecnologías utilizadas

- Python
- Pandas
- SQLite
- Streamlit
- Plotly
- Pytest

## Funcionalidades

- Carga de encuestas desde archivos CSV.
- Validación de campos obligatorios y valores vacíos.
- Detección de edades inválidas.
- Detección de registros duplicados.
- Validación de categorías y regiones permitidas.
- Almacenamiento de información en SQLite.
- Prevención de inserciones duplicadas.
- Análisis estadístico de los datos.
- Dashboard interactivo con filtros por región y edad.
- Visualización de indicadores y gráficos estadísticos.
- Pruebas automatizadas de validación e integración.

## Estructura del proyecto

```text
Datavoz/
├── data/
│   └── encuestas.csv
├── database/
│   ├── __init__.py
│   ├── conexion.py
│   ├── crear_tablas.py
│   └── inicializar.py
├── modules/
│   ├── __init__.py
│   ├── carga_datos.py
│   ├── validacion.py
│   ├── guardar_datos.py
│   ├── consultar_datos.py
│   └── analisis.py
├── tests/
│   ├── __init__.py
│   ├── test_validacion.py
│   └── test_integracion.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

La base de datos SQLite se genera durante la ejecución y no se incluye en el repositorio.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/6piotr/DataVoz.git
```

Ingresar a la carpeta:

```bash
cd DataVoz
```

Crear y activar un entorno virtual:

```bash
python -m venv venv
```

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Inicialización de la base de datos

Al iniciar la aplicación mediante Streamlit, el sistema comprueba si la tabla de encuestas existe y si contiene registros.

Si la base de datos está vacía, carga automáticamente los datos ficticios desde el archivo CSV, previa validación.

La base de datos SQLite se genera localmente y no se incluye en el repositorio de GitHub.

## Ejecución

Para iniciar el dashboard interactivo:

```bash
streamlit run app.py
```

La aplicación estará disponible en la dirección local que proporciona Streamlit al iniciar el servidor.

## Pruebas

Para ejecutar las pruebas automatizadas:

```bash
pytest -v
```

Las pruebas incluyen verificaciones de validación de datos y pruebas de integración de los procesos principales del sistema.

## Consideraciones sobre los datos

Los registros utilizados son ficticios y tienen fines exclusivamente educativos. No representan resultados electorales oficiales ni información real de personas.

La categoría "SERVEL" utilizada en la columna de fuentes es una etiqueta ficticia creada para representar una posible fuente institucional. No corresponde a datos obtenidos de registros individuales del Servicio Electoral de Chile ni implica una colaboración con dicha institución.

El proyecto no utiliza información personal real. Por este motivo, los resultados del dashboard sirven para demostrar el funcionamiento de los procesos de análisis y visualización, no para representar tendencias electorales reales.

## Seguridad y trazabilidad

El proyecto utiliza un archivo `.gitignore` para excluir archivos que no deben formar parte del repositorio, como la base de datos local, los entornos virtuales, los archivos temporales de Python y los archivos de configuración sensibles.

El flujo de procesamiento de los datos es el siguiente:

1. Carga de información desde el archivo CSV.
2. Validación de los registros.
3. Almacenamiento de los datos en SQLite.
4. Consulta y procesamiento mediante Pandas.
5. Análisis y generación de gráficos con Plotly.
6. Presentación de resultados en el dashboard de Streamlit.

## Despliegue

El proyecto se encuentra publicado mediante Streamlit Community Cloud y su código fuente está disponible en GitHub.

- Repositorio: https://github.com/6piotr/DataVoz

## Estado del proyecto

Proyecto académico desarrollado para integrar procesos de carga, validación, almacenamiento, análisis y visualización de datos mediante herramientas de desarrollo de software y análisis de información.