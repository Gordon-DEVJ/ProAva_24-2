# Logica.py

def suma_dos_numeros():                                 #Calcula y muestra la suma de dos numeros
    print("Ejercicio 1: Suma de dos numeros")

    n1 = int(input("Ingrese el primer numero: "))       #Primer numero
    n2 = int(input("Ingrese el segundo numero: "))      #Segundo numero
    print("El resultado de la suma es",n1+n2)           #Resultado

    print("")
    input("Presiona Enter para seguir...")              #Pausa
    print("")

def numero_par():                                       #Determina si un numeo es par o impar 
    print("Ejercicio 2: Numero Par o Impar")

    n = int(input("Ingrese el numero: "))
    if n % 2 == 0:                                      #Si el residuo es 0 al dividir entre 2 es par
        print(n," Es un numero par")
    else:
        print("El numero ",n, " es un numero impar")    
    
    print("")
    input("Presiona Enter para seguir...")              #Pausa
    print("")

def lista_numeros():                                    #Imprime una lista de numeros del 1 al 10
    print("Ejercicio 3: Listar los numeros del 1 al 10")

    for i in range ( 1, 11):                            #Ciclo for desde 1 hasta 10
        print(i, end=" ")                               #Imprime el valor i, seguido de un espacio.
    
    print("")
    input("Presiona Enter para seguir...")              #Pausa
    print("")

def suma_numeros():
    print("Ejercicio 4: Suma de listado de numeros")

    #Solicita los numeros que ingresara
    iteraciones = int(input("cuantos numeros ingresara?: "))
    nlista = []                                         #Inicio de una lista vacia
    for i in range(iteraciones):                        
        numero = int(input(f"Ingresa el número {i + 1}: "))
        nlista.append(numero)                           #Se añade el numero a la lista
    
    r = sum(nlista)                                     #Se suma los elementos de la lista
    print("La suma de los numeros ingresados es: ", r)
    
    print("")
    input("Presiona Enter para seguir...")              #Pausa
    print("")

def area_circulo():
    print("Ejercicio 5: Suma de listado de numeros")

    radio = float(input("Ingrese el Radio: "))
    area = 3.1416 * (radio**2)                          #Dice la formula: pi * area ^ 2
    print("El area de la circunferencia cuyo radio es", radio," es de ",area)
    
    print("")
    input("Presiona Enter para seguir...")              #Pausa
    print("")

def area_figuras():
    print("Switch para calcular el area de formas")
    
    print("1.\tCirculo")
    print("2.\tRectangulo")
    print("3.\tTriangulo")

    figura=int(input("Escoja la Figura: "))

    if figura == 1:
        radio = float(input("Ingrese el Radio: "))
        area = 3.1416 * (radio**2)                      #Dice la formula: pi * area ^ 2
        print("El area de la circunferencia cuyo radio es", radio," es de ",area)
    elif figura == 2:
        largo = float(input("Ingrese el Largo: "))
        ancho = float(input("Ingrese el Ancho: "))
        area = largo * ancho                            #Dice la formula: Largo * Ancho
        print("El area del rectangulo es: ", area)
    elif figura == 3:
        base = float(input("Ingrese el Largo: "))
        altura = float(input("Ingrese el Largo: "))
        area = base * altura / 2                        #Dice la formula base * altura / 2
        print("El area del triangulo es: ", area)
    else:
        print("Forma no valida.")
    
    print("")
    input("Presiona Enter para seguir...")              #Pausa
    print("")