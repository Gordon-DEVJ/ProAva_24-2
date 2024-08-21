#=============================== Funcion ===================================================================#
def agregar_nombre():
    #lower hace que el nombre sea puesto en minusculas
    nombre=input("Nombre del compañero de clase a agregar: ").lower()
    nombrecompañeros.append(nombre)
    p = nombrecompañeros.index(nombre)
    print(f"Nombre agregado, {nombre}, en la posicion {p}")
    
    input("Presione enter...")

def eliminar_nombre():
    # verificar si la lista esta vacia, si no, agregar el nombre
    if nombrecompañeros: #regresa true si hay un elemento en la lista
        print("Eliminando al ultimo compañero agregado")
        nombreborrado = nombrecompañeros.pop()
        print(f"{nombreborrado} Borrado de la pila")
    else:
        print("Pila vacia, no hay nombres a borrar")

    input("Presione enter...")

def mostrar_nombres():
    if nombrecompañeros: # por cada nombre en la pila va a escrribir la posicion en la pila y el nombre
        for nombre in (nombrecompañeros):
            p = nombrecompañeros.index(nombre)
            print(f"{p}\t{nombre}")
    else:
        print("Pila vacia, no hay nombres para mostrar.")

    input("Presione enter...")

def controlMenu():
    print("=======================================================================")
    print("\tTaller LIFO, Carlos Zarate")
    while True: 
        print("=======================================================================")
        print("\t\t     Menu Coleccion estudiantes")
        print("=======================================================================")
        print("\tOpciones")
        print("")
        print("1.\tAgregar Nombres")
        print("2.\tEliminar Nombres")
        print("3.\tMostrar Nombres")
        print("")
        print("5.\tSalir")
        print("=======================================================================")
        print("")

        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese enteros.")
            continue

        match opcion:
            case 1:
                agregar_nombre()
            case 2:
                eliminar_nombre()
            case 3:
                mostrar_nombres()
            case 5:
                exit()
            case _:
                print("Ingresa una opcion valida")
#=============================== Ejecucion ===================================================================#

#Iniciar pila vacia (lista en python, ya incluye append que seria push y pop que seria pop)
nombrecompañeros=[]

controlMenu()