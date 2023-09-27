"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
import traceback
from tabulate import tabulate  
default_limit= 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(list_type):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(list_type)
    return control
    
    


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 6")
    print("0- Salir")


def load_data(control, filename):
    """
    Carga los datos
    """
    return controller.load_data(control, filename)

def get_value(hash,key):
    return controller.get_value(hash,key)

def diccionario_tabulable(lista,filtros):
    
    new_dic = {}
    
    for dato in lt.iterator(lista):
        
        for llave in dato:
            if llave in filtros:
    
                if new_dic.get(llave,"no") == "no":
                    new_dic[llave] = [dato[llave]]
                else:
                    new_dic[llave].append(dato[llave])
    
    return new_dic
    
    
def lista_primeros_y_utlimos_3(lista):
        
    size = lt.size(lista)
    new_data = lt.newList("ARRAY_LIST")
     
    if size > 6:
        #primeros ordenados
        i = 1
        while i <= 3:
            elemento = lt.getElement(lista,i)
            lt.addLast(new_data, elemento)
            i += 1
        
        #ultimos ordenados 
        i = size - 2
        while i <= size:
            elemento = lt.getElement(lista, i)
            lt.addLast(new_data,elemento)
            i += 1
    else:
        new_data = lista
    
    return new_data
 
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    elemento = controller.buscar_elemento_por_id(control, id)
    
    if elemento:
        # Imprime los detalles del elemento
        print("Detalles del elemento con ID", id)
        print("Nombre:", elemento["nombre"])
        print("Descripción:", elemento["descripcion"])
        # Agrega aquí más detalles según la estructura de tu elemento
    else:
        print("Elemento con ID", id, "no encontrado")

def print_results(results):
    tamaño= lt.size(results)
    print("cantidad de resultados:", tamaño)
    print= lt.sublist(results, 0, 4)
    for i in range(3):
        ot= lt.getElement(results, tamaño-4+i)
        lt.addLast(print, ot)
    print(tabulate(lt.iterator(imp)))

def print_results(goalscores):
    tamaño= lt.size(goalscores)
    print("cantidad de goalscores:", tamaño)
    print= lt.sublist(goalscores, 0, 4)
    for i in range(3):
        ot= lt.getElement(goalscores, tamaño-4+i)
        lt.addLast(print, ot)
    print(tabulate(lt.iterator(imp)))

def print_results(shootouts):
    tamaño= lt.size(shootouts)
    print("cantidad de shootouts:", tamaño)
    print= lt.sublist(shootouts, 0, 4)
    for i in range(3):
        ot= lt.getElement(shootouts, tamaño-4+i)
        lt.addLast(print, ot)
    print(tabulate(lt.iterator(imp)))

def mini_diccionario_tabulable(answer,filtros):
    
    new_dic = {}
    for llave in answer:
        if llave in filtros:
            new_dic[llave] = [answer[llave]]
            
    return new_dic

def lista_tabulable_para_6(answer,filtros):
    new_list = []
    for llave in answer:
        if llave in filtros:
            new_list.append([llave,answer[llave]])

    return new_list


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    import controller
import model

def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    # Solicitar al usuario los parámetros de entrada
    N = int(input("Ingrese el número de últimos partidos a consultar: "))
    equipo = input("Ingrese el nombre del equipo (país de la selección nacional en inglés): ")
    condicion = input("Ingrese la condición del equipo (Local, Visitante, o Indiferente): ")

    # Obtener la lista de partidos desde el controlador (asegúrate de que controller.py tenga la función correspondiente)
    listaPartidos = controller.get_lista_partidos(control)

    # Llamar a la función del modelo para resolver el Requerimiento 1
    resultado = model.req_1(N, equipo, condicion, listaPartidos)

    if resultado:
        print("Resultado del Requerimiento 1:")
        print(f"Mostrando los últimos {N} partidos del equipo {equipo} como {condicion}:")
        print("Total de partidos encontrados:", resultado["total_partidos"])
        print("\nDetalles de los partidos:")
        for partido in resultado["partidos"]:
            print(f"Fecha del partido: {partido['fecha']}")
            print(f"Equipo local: {partido['equipo_local']}")
            print(f"Equipo visitante: {partido['equipo_visitante']}")
            print(f"País del encuentro: {partido['pais_encuentro']}")
            print(f"Ciudad del encuentro: {partido['ciudad_encuentro']}")
            print(f"Marcador del equipo local: {partido['marcador_local']}")
            print(f"Marcador del equipo visitante: {partido['marcador_visitante']}")
            print("-----------------------------")
    else:
        print("No se encontró el resultado del Requerimiento 1")





def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    # Solicitar al controlador los resultados del requerimiento 2
    N = int(input("Ingrese el número de goles a consultar: "))
    jugador = input("Ingrese el nombre completo del jugador: ")
    
    result = controller.req_2(N, jugador)

    if result:
        print(f"Total de anotaciones de {jugador}: {result['total_anotaciones']}")
        print("Primeros", N, "goles anotados por", jugador + ":")
        for gol in result["goles"]:
            print("Fecha del partido:", gol["fecha"])
            print("Equipo local:", gol["equipo_local"])
            print("Equipo visitante:", gol["equipo_visitante"])
            print("Equipo del jugador:", gol["equipo_jugador"])
            print("Minuto en el que se marcó el gol:", gol["minuto"])
            print("Tipo de anotación:", gol["tipo_anotacion"])
            print()

        # Imprime aquí el resultado del requerimiento 2 utilizando el resultado obtenido
    else:
        print(f"No se encontraron anotaciones para {jugador}")




def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    """
    Función que permite al usuario consultar los partidos disputados por un equipo durante un período específico.
    """
    print("Requerimiento No. 3: Consultar partidos por período y equipo")
    print("--------------------------------------------------------")

    # Solicitar nombre del equipo al usuario
    nombre_equipo = input("Ingrese el nombre del equipo: ")

    # Solicitar fecha inicial al usuario
    fecha_inicial = input("Ingrese la fecha inicial (formato YYYY-MM-DD): ")

    # Solicitar fecha final al usuario
    fecha_final = input("Ingrese la fecha final (formato YYYY-MM-DD): ")

    # Llamar a la función del controlador para ejecutar el requerimiento
    resultado = controller.req_3(control, nombre_equipo, fecha_inicial, fecha_final)

    # Imprimir los resultados
    if resultado:
        print("\nResultados:")
        print("Total de partidos disputados:", resultado["total_partidos"])
        print("Total de partidos como local:", resultado["total_local"])
        print("Total de partidos como visitante:", resultado["total_visitante"])

        # Imprimir los detalles de los partidos
        print("\nDetalles de los partidos:")
        for partido in resultado["partidos"]:
            print("Fecha:", partido.get("fecha", "Desconocido"))
            print("Marcador local:", partido.get("marcador_local", "Desconocido"))
            print("Marcador visitante:", partido.get("marcador_visitante", "Desconocido"))
            print("Equipo local:", partido.get("equipo_local", "Desconocido"))
            print("Equipo visitante:", partido.get("equipo_visitante", "Desconocido"))
            print("País del encuentro:", partido.get("pais_encuentro", "Desconocido"))
            print("Ciudad del encuentro:", partido.get("ciudad_encuentro", "Desconocido"))
            print("Nombre del torneo:", partido.get("nombre_torneo", "Desconocido"))
            print("Anotación de penal:", partido.get("anotacion_penal", "No"))
            print("Anotación de autogol:", partido.get("autogol", "No"))
            print("\n")
    else:
        print("No se encontraron resultados para la consulta.")




def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    def print_req_6(resultado):
     """
     Función que imprime la solución del Requerimiento 6 en consola
    """
    if resultado:
        print("Resultado del Requerimiento 6:")
        print(f"Total de equipos involucrados en el torneo: {resultado['total_equipos']}")
        print(f"Total de encuentros disputados en el período: {resultado['total_encuentros']}")
        print(f"Total de países involucrados en el torneo: {resultado['total_paises']}")
        print(f"Total de ciudades involucradas en el torneo: {resultado['total_ciudades']}")
        print(f"Nombre de la ciudad con más partidos disputados: {resultado['ciudad_mas_partidos']}")
        print("\nLista de los mejores equipos:")
        
        for i, equipo in enumerate(resultado['equipos'], start=1):
            print(f"\nEquipo #{i}: {equipo['nombre']}")
            print(f"Total de puntos obtenidos: {equipo['puntos']}")
            print(f"Diferencia de goles: {equipo['diferencia_goles']}")
            print(f"Total de partidos disputados: {equipo['partidos_disputados']}")
            print(f"Total de puntos obtenidos desde la línea penal: {equipo['puntos_penal']}")
            print(f"Total de puntos recibidos por autogol: {equipo['puntos_autogol']}")
            print(f"Total de victorias: {equipo['victorias']}")
            print(f"Total de empates: {equipo['empates']}")
            print(f"Total de derrotas: {equipo['derrotas']}")
            print(f"Total de goles obtenidos por sus jugadores: {equipo['goles_obtenidos']}")
            print(f"Total de goles recibidos por el equipo: {equipo['goles_recibidos']}")
            
            jugador_destacado = equipo['jugador_destacado']
            print("\nJugador Destacado:")
            print(f"Nombre del jugador: {jugador_destacado['nombre']}")
            print(f"Total de goles anotados: {jugador_destacado['goles_anotados']}")
            print(f"Total de partidos donde anotó un gol: {jugador_destacado['partidos_con_gol']}")
            print(f"Promedio de tiempo para anotar goles (en minutos): {jugador_destacado['promedio_minutos_por_gol']}")

        # Si hay más de 6 equipos, mostrar solo los 3 primeros y los 3 últimos
        if len(resultado['equipos']) > 6:
            print("\n(Solo se muestran los 3 primeros y los 3 últimos equipos)")
    else:
        print("No se encontró el resultado del Requerimiento 6")




# Se crea el controlador asociado a la vista
control = new_controller("ARRAY_LIST")

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
