# DataVoz | Sistema de análisis de encuestas

## Descripción

DataVoz es un sistema de análisis de encuestas desarrollado en Python. Su objetivo es cargar, validar, almacenar y analizar información mediante una base de datos SQLite y un dashboard interactivo.

El proyecto utiliza datos ficticios para representar un escenario de análisis de preferencias políticas e intención de voto.

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
- Pruebas automatizadas de validación e integración.

## Estructura del proyecto

```text
Datavoz/
├── data/
├── database/
├── modules/
├── tests/
├── app.py
├── requirements.txt
└── README.md
```

## Instalación

Clonar el repositorio y acceder a la carpeta del proyecto.

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Para cargar las encuestas:

```bash
python -m modules.carga_datos
```

Para iniciar el dashboard:

```bash
streamlit run app.py
```

## Pruebas

Para ejecutar las pruebas automatizadas:

```bash
pytest -v
```

## Consideraciones sobre los datos

Los registros utilizados son ficticios y tienen fines exclusivamente educativos. No representan resultados electorales oficiales ni información real de personas.

## Estado del proyecto

Proyecto académico en desarrollo para integrar procesos de carga, validación, almacenamiento, análisis y visualización de datos.