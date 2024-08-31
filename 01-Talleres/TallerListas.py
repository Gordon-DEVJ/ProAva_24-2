import os # para limpiar la consola
#=============================== Funcion ===================================================================#

#=============================== Listas  ===================================================================#

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
        print("Limpiado...")

def agregar_inicio():

    nombre=input("Nombre del compañero de clase a agregar: ").lower()
    nombrecompañeros.insert(0,nombre)
    p = nombrecompañeros.index(nombre)
    print(f"Nombre agregado, {nombre}, en la posicion {p}")
    
    input("Presione enter...")

def agregar_final():

    nombre=input("Nombre del compañero de clase a agregar: ").lower()
    nombrecompañeros.append(nombre)
    p = nombrecompañeros.index(nombre)
    print(f"Nombre agregado, {nombre}, en la posicion {p}")
    
    input("Presione enter...")

def agregar_posicion():

    nombre=input("Nombre del compañero de clase a agregar: ").lower()
    p = int (input("Ingrese la posicion deseada"))
    nombrecompañeros.insert((p-1),nombre)
    print(f"Nombre agregado, {nombre}, en la posicion {p}")
    
    input("Presione enter...")

def eliminar_inicio():

    if nombrecompañeros: #regresa true si hay un elemento en la lista
        print("Eliminando al primer compañero agregado")
        nombreborrado = nombrecompañeros.pop(0)
        print(f"{nombreborrado} Borrado de la primera posicion")
    else:
        print("Lista vacia, no hay nombres a borrar")

    input("Presione enter...")

def eliminar_final():

    if nombrecompañeros: #regresa true si hay un elemento en la lista
        print("Eliminando al ultimo compañero agregado")
        nombreborrado = nombrecompañeros.pop()
        print(f"{nombreborrado} Borrado de la primera posicion")
    else:
        print("Lista vacia, no hay nombres a borrar")

    input("Presione enter...")

def eliminar_posicion():

    if nombrecompañeros: #regresa true si hay un elemento en la lista
        p = int (input("Ingrese la posicion deseada a borrar"))
        print(f"Eliminando el dato en la posicion {p}")
        nombreborrado = nombrecompañeros.pop(p-1)
        print(f"{nombreborrado} Borrado de la posicion {p}")
    else:
        print("Lista vacia, no hay nombres a borrar")

    input("Presione enter...")

def eliminar_valor():

    if nombrecompañeros:
        v = str(input("Nombre del compañero de clase a eliminar: ").lower())
        if v in nombrecompañeros:
            nombrecompañeros.remove(v)
            print("Nombre borrado")
        else:
            print("Nombre no existe")
    else:
        print("Lista vacia, no hay nombres a borrar")

    input("Presione enter...")

def mostrar_nombres():
    if nombrecompañeros: # por cada nombre en la Lista va a escrribir la posicion en la Lista y el nombre
        for nombre in (nombrecompañeros):
            p = nombrecompañeros.index(nombre)
            print(f"{p}\t{nombre}")
    else:
        print("Lista vacia, no hay nombres para mostrar.")

    input("Presione enter...")

def controlMenu():
    
    print("=======================================================================")
    print("\tTaller Listas, Carlos Zarate")
    while True: 
        limpiar_pantalla()
        print("=======================================================================")
        print("\t\t     Menu Coleccion estudiantes | Uso de listas")
        print("=======================================================================")
        print("\tOpciones")
        print("")
        print("\t\tAgregar Nombres")
        print("")
        print("1.\tAgregar Nombres al inicio")
        print("2.\tAgregar Nombres al final")
        print("3.\tAgregar Nombres por posicion")
        print("")
        print("\t\tEliminar Nombres")
        print("")
        print("4.\tEliminar Nombres al inicio")        
        print("5.\tEliminar Nombres al final")
        print("6.\tEliminar Nombres por posicion")
        print("")
        print("\t\tOtros")
        print("")
        print("7.\tMostrar nombres")       
        print("")
        print("8.\tSalir")
        print("=======================================================================")
        print("")

        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese enteros.")
            continue

        match opcion:
            case 1:
                agregar_inicio()
            case 2:
                agregar_final()
            case 3:
                agregar_posicion()
            case 4:
                eliminar_inicio()
            case 5:
                eliminar_final()
            case 6:
                eliminar_posicion()
            case 7:
                mostrar_nombres()
            case 8:
                exit()
            case _:
                print("Ingresa una opcion valida")

#=============================== Ejecucion ===================================================================#

#Iniciar Lista vacia (lista en python, ya incluye append que seria push y pop que seria pop)
nombrecompañeros=[]

controlMenu()