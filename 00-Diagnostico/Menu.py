# Examen Diagnostico

#Menu.Py
from Logica import *
 
def control_menu():
    
    #While para que el menu se muestre despues de usar una funcion.
    while True: 
        print("=======================================================================")
        print("\t\t     Menu Examen Diagnostico")
        print("=======================================================================")
        print("\tEjercicios")
        print("")
        print("1.\tSuma de dos numeros")
        print("2.\tNumero par o impar")
        print("3.\tListar los numeros del 1 al 10")
        print("4.\tSuma de listado de numeros")
        print("5.\tFuncion para calcular el area de un circulo")
        print("6.\tSwitch para calcular el area de figuras")
        print("")
        print("=======================================================================")
        print("")

        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese enteros.")
            continue

        #Python no tiene switch case como java.        
        #Diccionario de funciones
        lista_ejercicios = {
            1: suma_dos_numeros,
            2: numero_par,
            3: lista_numeros,
            4: suma_numeros,
            5: area_circulo,
            6: area_figuras,
        } #Nombre exacto de la funcion de cada ejercicio

        llamada = lista_ejercicios.get(opcion, None)
        if llamada is None:
            print("Opcion no Valida, ingrese un valor entre 1 y 6")
        else:
            llamada()

#=============================== Ejecucion ===================================================================#

control_menu()