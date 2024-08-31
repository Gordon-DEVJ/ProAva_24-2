import os # para limpiar la consola
#=============================== Funcion ===================================================================#

def clean_display():
    if os.name == 'nt':
        os.system('cls')
        print("Cleaning...")

def pause():
    input("Type Enter...")

def add_income():

    try:
        new_income = float(input("Enter new Income: "))
        incomes.append(new_income)
        print(f"Income Added")
    except ValueError:
        print("Type a valid numeric value...")
    pause()

def add_expense():

    try:
        new_expense = float(input("Enter new Expense: "))
        expenses.append(new_expense)
        print(f"Expense Added")
    except ValueError:
        print("Type a valid numeric value...")
    pause()

def show_lists():

    if not incomes and not expenses:
        print("Lists empty")

    else:
        if incomes:
            print("- Incomes")
            print("")
            for income in incomes:
                p = incomes.index(income)
                print(f"{p+1}\t{income}")
        else:
            print("Incomes empty")

        if expenses:
            print("- Expenses")
            print("")
            for expense in expenses:
                p = expenses.index(expense)
                print(f"{p+1}\t{expense}")
        else:
            print("Expenses empty")
    
    pause()

def calculatelist():
    if not incomes and not expenses:
        print("Lists empty")
    else: 
        total_i = sum(incomes)
        total_e = sum(expenses)
        dif = total_i - total_e
        if dif > 0:
            print(f"gain of {dif}")
        elif dif < 0:
            print(f"loss of {abs(dif)}")
        else:
            print("no gains no losses")
    pause()

def controlMenu():
    
    print("=======================================================================")
    print("\tQUIZ #1, Carlos Zarate")
    while True: 
        clean_display()
        print("=======================================================================")
        print("\t\t     Expenses & Incomes")
        print("=======================================================================")
        print("\tOptions")
        print("")
        print("1.\tAdd Incomes")
        print("2.\tAdd Expenses")
        print("3.\tShow Lists")
        print("4.\tCalculate Lists")       
        print("")
        print("8.\tExit")
        print("=======================================================================")
        print("")

        try:
            opcion = int(input("Type a value option: "))
        except ValueError:
            print("Type Int Values")
            continue

        match opcion:
            case 1:
                add_income()
            case 2:
                add_expense()
            case 3:
                show_lists()
            case 4:
                calculatelist()
            case 8:
                exit()
            case _:
                print("ype a value option: ")

#=============================== Ejecucion ===================================================================#

incomes=[]
expenses=[]

controlMenu()
