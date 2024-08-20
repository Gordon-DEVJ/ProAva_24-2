#=============================== Funcion ===================================================================#

# La tabla la generara una funcion.
def gen_tabla(n):
    # Ciclo For que itera del 1 al 10
    for i in range (1,11):
        r = n * i
        # Evalua si es par
        if r % 2==0:
            print(f"{n}x{i}={r} es par")
        else:
            print(f"{n}x{i}={r} es impar")
    # Pausa
    input("Enter para continuar con otro ejercicio...")


#=============================== Ejecucion ===================================================================#
print("=======================================================================")
print("\tTaller Condicionales / For, Carlos Zarate")
print("=======================================================================")

while True:
    print("")
    print("Generador de tabla de multiplicar y señala si es par o no par")
    # Para evitar fallas uso un try except
    try:
        n = int(input("Ingrese una opcion: "))
        if n < 0:
            print("Ingrese enteros positivos.")
        else: 
            gen_tabla(n)
    except ValueError:
        print("Ingrese enteros positivos.")