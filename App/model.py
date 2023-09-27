"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from tabulate import tabulate
from datetime import datetime 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(list_type):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {"resultados":None, "goles":None, "penaltis":None}
    data_structs["resultados"] = lt.newList(list_type)
    data_structs["goles"] = lt.newList(list_type)
    data_structs["penaltis"] = lt.newList(list_type)
    
    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    d= new_data(id, data)
    lt.addLast(data_structs["data1results"],d)
    return data_structs


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    data = {
        "id": id,
        "info": info
    }
    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    
    return lt.getElement(data_structs["data"], id)


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs["data"])


def req_1(N, partido, condicion):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    # Filtrar la lista de partidos según la condición
    data_structs1= data_structs["resultados"]
    partidosFiltrados = [partido for partido in data_structs1  if condicion in partido['condicion']]

    # Ordenar los partidos cronológicamente (del más reciente al más antiguo)
    partidosFiltrados.sort(key=lambda partido: partido['fecha'], reverse=True)

    # Limitar la lista a los últimos N partidos
    partidosLimitados = partidosFiltrados[:N]

    # Preparar la respuesta
    respuesta = {
        "total_partidos": len(partidosFiltrados),
        "partidos": []
    }

    # Agregar detalles de los partidos a la respuesta
    for partido in partidosLimitados:
        detalle_partido = {
            "fecha": partido.get("fecha", "Desconocido"),
            "equipo_local": partido.get("equipo_local", "Desconocido"),
            "equipo_visitante": partido.get("equipo_visitante", "Desconocido"),
            "pais_encuentro": partido.get("pais_encuentro", "Desconocido"),
            "ciudad_encuentro": partido.get("ciudad_encuentro", "Desconocido"),
            "marcador_local": partido.get("marcador_local", "Desconocido"),
            "marcador_visitante": partido.get("marcador_visitante", "Desconocido"),
        }
        respuesta["partidos"].append(detalle_partido)

    # Mostrar solo los tres primeros y tres últimos elementos si la respuesta es larga
    if len(respuesta["partidos"]) > 6:
        respuesta["partidos"] = respuesta["partidos"][:3] + respuesta["partidos"][-3:]

    return respuesta



def req_2(jugador, N, listaPartidos):
    """
    Función que soluciona el requerimiento 2
    """
    # Filtrar la lista de partidos para encontrar los goles anotados por el jugador
    goles_del_jugador = []
    for partido in listaPartidos:
        for gol in partido["goles"]:
            if gol["jugador"] == jugador:
                goles_del_jugador.append({
                    "fecha": partido["fecha"],
                    "equipo_local": partido["equipo_local"],
                    "equipo_visitante": partido["equipo_visitante"],
                    "equipo_jugador": gol.get("equipo_jugador", "Desconocido"),
                    "minuto": gol.get("minuto", "Desconocido"),
                    "tipo_anotacion": gol.get("tipo_anotacion", "Desconocido"),
                })

    # Ordenar los goles del jugador cronológicamente (del partido más antiguo al más reciente y según el minuto)
    goles_del_jugador.sort(key=lambda gol: (gol["fecha"], gol["minuto"]))

    # Limitar la lista a los primeros N goles
    goles_limitados = goles_del_jugador[:N]

    # Preparar la respuesta
    respuesta = {
        "total_anotaciones": len(goles_del_jugador),
        "goles": goles_limitados
    }

    return respuesta


def req_3(nombre_equipo, fecha_inicial, fecha_final):
     """
     Función que consulta los partidos disputados por un equipo durante un período específico.
     """
    # Inicializar listas para almacenar los partidos
     partidos_totales = []
     partidos_local = []
     partidos_visitante = []

    # Recorrer la lista de partidos y filtrar los que cumplen con el período y el equipo
     for partido in data_structs["resultados"]:
        fecha_partido = partido.get("fecha", "")
        equipo_local = partido.get("equipo_local", "")
        equipo_visitante = partido.get("equipo_visitante", "")

        # Verificar si el equipo participó en el partido
        if nombre_equipo in (equipo_local, equipo_visitante):
            # Verificar si el partido está dentro del período especificado
            if fecha_inicial <= fecha_partido <= fecha_final:
                partidos_totales.append(partido)

                # Determinar si el equipo fue local o visitante
                if nombre_equipo == equipo_local:
                    partidos_local.append(partido)
                else:
                    partidos_visitante.append(partido)

    # Ordenar los partidos por fecha (del más reciente al más antiguo)
     partidos_totales.sort(key=lambda partido: partido["fecha"], reverse=True)

    # Preparar la respuesta
     respuesta = {
        "total_partidos": len(partidos_totales),
        "total_local": len(partidos_local),
        "total_visitante": len(partidos_visitante),
        "partidos": partidos_totales
    }

     return respuesta

def req_4(torneo, fechainicial, fechafinal):
    #inicializar listas para almacenar los datos
    total_partidos = []
    total_paises = []
    total_ciudades = []
    total_partidopenal = []
    #recorrer la lista de partidos y filtrar los que cumplen con el periodo de tiempo
    for partido in listapartidos:
        fecha_partido = partido.get("fecha","")
        pais = partido.get("pais", "")
        ciudad = partido.get("ciudad", "")
        if fechainicial <= fecha_partido and fechafinal >= fecha_partido:
            total_partidos.append(partido)
        if pais not in total_paises:
            total_paises.append(pais)
        if ciudad not in total_ciudades:
            total_ciudades.append(ciudad)

#Completar con calculos 
def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    def req_6(N, nombre_torneo, fecha_inicial, fecha_final):
     """
    Clasifica los N mejores equipos de un torneo en un período específico.
    """
    # Crear una estructura de datos para almacenar los resultados
    resultado = {
        "total_equipos": 0,
        "total_encuentros": 0,
        "total_paises": 0,
        "total_ciudades": 0,
        "ciudad_mas_partidos": "Desconocido",
        "equipos": []
    }

    # Obtener la lista de equipos del torneo
    equipos = obtener_equipos_por_torneo(nombre_torneo)

    # Obtener la lista de partidos dentro del período especificado
    partidos_en_periodo = obtener_partidos_en_periodo(fecha_inicial, fecha_final)

    # Calcular estadísticas para cada equipo
    for equipo in equipos:
        estadisticas_equipo = calcular_estadisticas_equipo(equipo, partidos_en_periodo)
        resultado["equipos"].append(estadisticas_equipo)

    # Ordenar los equipos por criterio compuesto
    resultado["equipos"].sort(key=lambda equipo: (
        -equipo["puntos"],
        -equipo["diferencia_goles"],
        equipo["goles_por_penal"],
        equipo["partidos_disputados"],
        equipo["autogoles"]
    ))

    # Limitar la lista de equipos a los N mejores
    resultado["equipos"] = resultado["equipos"][:N]

    # Rellenar otros campos de resultado (total de equipos, total de encuentros, etc.)
    resultado["total_equipos"] = len(equipos)
    resultado["total_encuentros"] = len(partidos_en_periodo)
    resultado["total_paises"] = len(obtener_paises_en_torneo(nombre_torneo))
    resultado["total_ciudades"] = len(obtener_ciudades_en_torneo(nombre_torneo))
    resultado["ciudad_mas_partidos"] = obtener_ciudad_mas_partidos(nombre_torneo)

    return resultado


# Funciones utilizadas para comparar elementos dentro de una lista

def compare_results(registerA, registerB):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    dateA= "Objeto Date"
    dateB= "Objeto Date"
    if dateA == dateB:
       if registerA['home_score']== registerB['home_score']:
           return int(registerA['away_score'])> int(registerB['away_score'])
       else:
           return int(registerA['home_socre'])>int(registerB['home_score'])
    else:
        return dateA > dateB

def compare_goalscores(registerA, registerB):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    dateA= "Objeto Date"
    dateB= "Objeto Date"
    if dateA == dateB:
       if registerA['home_score']== registerB['home_score']:
           return int(registerA['minute'])> int(registerB['minute'])
       else:
           return int(registerA['home_socre'])>int(registerB['home_score'])
    else:
        return dateA > dateB

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento para results 

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    dateA = datetime.strptime(data_1["date"], "%Y-%m-%d")
    dateB = datetime.strptime(data_2["date"], "%Y-%m-%d")

    if dateA == dateB:
        if int(data_1["home_score"]) > int(data_2["home_score"]):
            return True
        else:
            return False
    elif dateA > dateB:
        return True
    else:
        return False
 


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    list_1=data_structs["resultados"]

    return sa.sort(list_1,sort_criteria)


   
