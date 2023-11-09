print("\n                                    Ejercicio Propuesto                                ")
#importamos libreria para la fecha y la tome directamente del sistema (dia/mes/año)(hora,segundos)
from datetime import datetime
from datetime import date
#Obtiene la fecha y hora actual del sistema y la almacena en la variable fecha
fecha= datetime.now()

#diccionario vacio para almacenar informacion de los equipos
equipos = {}

#lista vacia que almacenara las novedades sobre los equipos
novedades = []


#funcion para agregar un equipo y lo va a almacenar(agregar) al diccionario
#(lower: va apermitir que el usuario digite mayusculas o minusculas)
def agregarEquipo():
    equipoId =input("Ingrese el ID del equipo: ")
    nAmbiente = int(input("Ingrese el numero del ambiente al que pertenece: "))
    disCargador = input("¿Tiene cargador? si/no: ").lower()
    disMouse = input("¿Tiene mouse? si/no: ").lower()
    equipos[equipoId] = {"cargador": disCargador, "mouse": disMouse, "ambiente":nAmbiente}
    #agrega la información del equipo al diccionario equipos utilizando el ID del equipo como clave.
    #el valor asociado a la clave es otro diccionario que contiene informacion sobre el cargador, el mouse y el ambiente del equipo.
    print("Equipo agregado")


#funcion para agregar novedades y lo almacenara en la lista vacia de novedades
def agregarNovedad():
    equipoId = input("Ingrese el ID del equipo al que desea agregar una novedad: ")
#verifica si el ID del equipo ingresado está presente en el diccionario equipos.
    if equipoId in equipos:
        descripcion = input("Ingrese la descripcion de la novedad: ")
#agrega un nuevo diccionario a la lista novedades, que contiene información sobre la novedad, como el ID del equipo, la fecha actual y la descripción ingresada.
        novedades.append({"equipo ID": equipoId, "fecha": str(fecha), "descripcion": descripcion})
        print("Novedad agregada")
    else:
        print("Equipo no encontrado en la lista")


#funcion para buscar un equipo mediante el ID en el diccionario
def buscarEquipo():
    equipoId = input("Ingrese el ID del equipo que desea buscar: ")
    if equipoId in equipos:
#si el equipo se encuentra en la lista, imprime la lista completa de novedades.
        print(novedades)
    else:
        print("Equipo no encontrado")


#funcion que va a mostrar las novedades del equipo que desee mediante el id
def mostrarReporte():
    equipoId = input("Ingrese el ID del equipo para ver los reportes: ")
    print(f"Reportes del equipo con ID {equipoId}:")
#itera a traves de cada reporte en la lista novedades
    for reporte in novedades:
        #verifica si el ID del equipo en el reporte coincide con el ID ingresado por el usuario.
        if reporte["equipo ID"] == equipoId:
            print(f"Fecha: {reporte['fecha']}")
            print(f"Descripcion: {reporte['descripcion']}")
        else:
            print("El equipo no esta en la lista de agregados o no presenta novedades")
 
 
#funcion para modificar equipos que se encuentren dentro del diccionario 
def modificarEquipo():
    equipoId = input("Ingrese el ID del equipo a modificar: ")
    nuevoEstado = input("Ingrese el nuevo estado: ")
    #verifica
    if equipoId in equipos:
        #si el equipo se encuentra en la lista, modifica el valor asociado a la clave 'estado' en el diccionario del equipo con el nuevo estado.
        equipos[equipoId]['estado'] = nuevoEstado
        print(f"Se modificó el estado del equipo con ID {equipoId} a {nuevoEstado}")
    else:
        print(f"No existe un equipo con ID {equipoId}")


#funcion para eliminar cualquier equipo que este dentro del diccionario
def eliminarEquipo():
    equipoId = input("Ingrese el ID del equipo a eliminar: ")
    if equipoId in equipos:
        #si el equipo se encuentra en la lista de los equipos agregados, utiliza la instruccion 'del' para eliminar la entrada correspondiente al ID del equipo.
        del equipos[equipoId]
        print(f"Se eliminó el equipo con ID {equipoId}")
    else:
        print(f"No existe un equipo con ID {equipoId}")


#funcion que va a imprimir la lista de equipos que se ingresaron y se almacenaron en el diccionario    
def mostrarEquipos():
    print("Lista de equipos:")
    #itera a traves de cada par clave-valor en el diccionario equipos
    for equipoId, equipoInfo in equipos.items():
        print(f"Equipo ID: {equipoId}")
        print(f"Cargador: {equipoInfo['cargador']}")
        print(f"Mouse: {equipoInfo['mouse']}")
        print()

#se inicia un bucle infinito que presenta un menu de opciones al usuario
while True:
    print("\nOpciones")
    print("1. Agregar equipo")
    print("2. Agregar novedad")
    print("3. Buscar equipo")
    print("4. Mostrar reportes de un equipo")
    print("5. Modificar equipo")
    print("6. Eliminar equipo")
    print("7. Mostrar lista de equipos")
    print("8. Salir")
 
#if y elif ejecutan diferentes funciones según la opción seleccionada por el usuario.  
    opcion = input("Seleccione una opcion: ")
    if opcion == '1':
        agregarEquipo()
    elif opcion == '2':
        agregarNovedad()
    elif opcion == '3':
        buscarEquipo()
    elif opcion == '4':
        mostrarReporte()
    elif opcion == '5':
        modificarEquipo()
    elif opcion == '6':
        eliminarEquipo()
    elif opcion == '7':
        mostrarEquipos()
    elif opcion == '8':
        print("Salio del programa")
        break #sale del bucle infinito, terminando el programa
    else:
        print("Opcion no valida, elija una opcion valida")
        
#Maria Jose Perez
#Nataly Montaña
        