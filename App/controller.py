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
 """

import config as cf
import model
import time
import csv
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(list_type):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {"model":None}
    control["model"] = model.new_data_structs(list_type)
    return control


# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    catalog = control['model']
    contentfile = cf.data_dir + filename
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    
    for content in input_file:
        datos= model.add_data(catalog, content)
    model.sort(datos["data"])   
    delta_t = sort(catalog)
    
    return  model.sort_criteria(catalog),delta_t

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    data = model.get_data(control["model"], id)
    return data
def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    dato = model.req_1(control, anio, cod)
    start_time = get_time()
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return dato, delta_t


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    dato = model.req_2(control, anio, cod)
    start_time = get_time()
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return dato, delta_t


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    dato = model.req_3(control, anio, cod)
    start_time = get_time()
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return dato, delta_t



def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    dato = model.req_1(control, anio, cod)
    start_time = get_time()
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return dato, delta_t


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
