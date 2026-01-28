def analisis_incidentes(lista_incidentes):


    """Analiza y procesa una lista de incidentes operativos agrupando por sector. Devuelve un informe final por sector con el total de incidentes y la cantidad de registros considerados válidos.
     
    Reglas:
    Se consideran válidos:
    -Registros con estado "válido"
    -Incidentes mayores a 0
    -La prioridad es media o alta
    -Los registros con clave faltante, se ignoran
    
    Estructura de salida:
    
    {
        "Sector": {
            "total_incidentes": int,
            "registros_contados": int,
            "promedio_incidentes": float
        }
    }
    
    """

    #validacion lista vacía
    if not lista_incidentes:
        return {}
    
    informe_final = {}


    for inc in lista_incidentes:

        #validacion de claves
        if "sector" not in inc or "incidentes" not in inc or "prioridad" not in inc or "estado" not in inc:
            continue

        #filtro de registros válidos
        if inc["estado"] == "valido" and inc["incidentes"] > 0 and (inc["prioridad"] == "media" or inc["prioridad"] == "alta"):


            sector = inc["sector"]
            incidente = inc["incidentes"]
            

            #creación vs actualización
            if sector not in informe_final:
                informe_final[sector] = {"total_incidentes": incidente,
                                        "registros_contados": 1
                                        }
                        
            else:
                informe_final[sector]["total_incidentes"] += incidente
                informe_final[sector]["registros_contados"] += 1

    # cálculo del promedio
    for sector in informe_final:

        total_incidentes = informe_final[sector]["total_incidentes"]
        registros_contados = informe_final[sector]["registros_contados"]

        #validacion por cero
        if registros_contados > 0:
            informe_final[sector]["promedio_por_registros"] = total_incidentes / registros_contados


    return informe_final
        

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
print(informe_final)