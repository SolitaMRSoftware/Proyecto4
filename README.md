# Proyecto 4 - Análisis de incidentes

Este proyecto está desarrollado en Python. Analiza y procesa una lista de incidentes operativos **agrupando por sector**. 
    
## Funcionalidad principal

- Se consideran:
    - Registros con estado "válido"
    - Incidentes mayores a 0
    - La prioridad es media o alta
    - Los registros con clave faltante, se ignoran


- Retorna:

  - Un diccionario con un informe final por sector con el total de incidentes y la cantidad de registros considerados válidos.


## Estructura de salida:
    
    {
        "Sector": {
            "total_incidentes": int,
            "registros_contados": int,
            "promedio_incidentes": float
        }
    }


## Ejemplo de uso

```python

# Crear un archivo nuevo en la misma carpeta, por ejemplo test.py
from analisis_incidentes.py import analisis_incidentes


incidentes_operativos = [
    {"sector": "IT", "incidentes": 3, "prioridad": "media", "estado": "valido"},
    {"sector": "Soporte", "incidentes": 0, "prioridad": "alta", "estado": "valido"},
    {"sector": "IT", "incidentes": 2, "prioridad": "alta", "estado": "valido"},
    {"sector": "RRHH", "incidentes": 1, "prioridad": "media", "estado": "invalido"},
    {"sector": "Logística", "incidentes": 4, "prioridad": "alta", "estado": "valido"},
    {"sector": "Soporte", "incidentes": 2, "prioridad": "media", "estado": "valido"},
    {"sector": "IT", "incidentes": 1, "prioridad": "baja", "estado": "valido"},
    {"sector": "Logística", "incidentes": 3, "prioridad": "media", "estado": "valido"},
    {"sector": "IT", "incidentes": 0, "prioridad": "media", "estado": "valido"},
    {"sector": "Soporte", "incidentes": 1, "prioridad": "alta", "estado": "valido"},
    {"sector": "Compras", "incidentes": 2, "prioridad": "media", "estado": "valido"},
    {"sector": "IT", "incidentes": 2, "prioridad": "alta"},  # falta estado
    {"sector": "RRHH", "incidentes": 3, "prioridad": "alta", "estado": "valido"},
    {"incidentes": 1, "prioridad": "media", "estado": "valido"},  # falta sector
]

informe_final = analisis_incidentes(incidentes_operativos)
print(informe_final) #Salida esperada {'IT': {'total_incidentes': 5, 'registros_contados': 2, 'promedio_por_registros': 2.5}, 'Logística': {'total_incidentes': 7, 'registros_contados': 2, 'promedio_por_registros': 3.5}, 'Soporte': {'total_incidentes': 3, 'registros_contados': 2, 'promedio_por_registros': 1.5}, 'Compras': {'total_incidentes': 2, 'registros_contados': 1, 'promedio_por_registros': 2.0}, 'RRHH': {'total_incidentes': 3, 'registros_contados': 1, 'promedio_por_registros': 3.0}}

```