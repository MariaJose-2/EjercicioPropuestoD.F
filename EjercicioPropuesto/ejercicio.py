#Se debe desarrollar una aplicación en Python que permita llevar el control de novedades de los equipos que se encuentran en los diferentes ambientes.La aplicación debe permitir:
#-Agregar los equipos de cómputo con su ID y dispositivos (cargador y mouse) utilizando un diccionario para almacenar la información de cada equipo.
#-Agregar novedades sobre los equipos de cómputo, fecha y descripción.
#-Buscar un equipo de cómputo utilizando su ID y mostrar su información.
#-Mostrar un reporte de equipos que presentan novedades utilizando una función que recorra la lista de novedades y muestre solo las que correspondan a equipos que presentan novedades.
#-Se deben crear funciones para agregar, modificar y eliminar equipos, así como para mostrar la lista completa de equipos y su estado actual.

#diccionario para almacenar informacion de los equipos
equipos = {}

#lista que almacenara las novedades
novedades = []

#funcion para agregar un equipo
def agregarEquipo():
    equipoId = input("Ingrese el ID del equipo: ")
    disCargador = input("Ingrese el estado del cargador: ")
    disMouse = input("Ingrese el estado del mouse: ")
    equipos[equipoId] = {"cargador": disCargador, "mouse": disMouse}
    print("Equipo agregado")

#funcion para agregar novedades
def agregarNovedad():
    equipoId = input("Ingrese el ID del equipo al que desea agregar una novedad: ")
    fecha = input("Ingrese la fecha de la novedad: ")
    descripcion = input("Ingrese la descripción de la novedad: ")
    novedades.append({"equipo ID": equipoId, "fecha": fecha, "descripcion": descripcion})
    print("Novedad agregada")

#funcion para buscar un equipo mediante el ID
def buscarEquipo():
    equipoId = input("Ingrese el ID del equipo que desea buscar: ")
    equipo = equipos.get(equipoId)
    if equipo:
        print(f"Equipo ID: {equipoId}")
        print(f"Cargador: {equipo['cargador']}")
        print(f"Mouse: {equipo['mouse']}")
    else:
        print("Equipo no encontrado")

#funcion que va a mostrar las novedades del equipo que desee mediante el id
def mostrarReporte():
    equipoId = input("Ingrese el ID del equipo para ver los reportes: ")
    print(f"Reportes del equipo con ID {equipoId}:")
    for reporte in novedades:
        if reporte["equipo ID"] == equipoId:
            print(f"Fecha: {reporte['fecha']}")
            print(f"Descripcion: {reporte['descripcion']}")

#funcion que va a mostrar la lista de equipos que ingreso el usuario
def mostrarEquipos():
    print("Lista de equipos:")
    for equipoId, equipoInfo in equipos.items():
        print(f"Equipo ID: {equipoId}")
        print(f"Cargador: {equipoInfo['cargador']}")
        print(f"Mouse: {equipoInfo['mouse']}")
        print()

#nos falta codigo para utilizar un ciclo y mostrar opciones para que el usuario elija.
#falta un mensaje en la funcion de mostrar novedades