from partida import Partida
from varlog import sortida
import os

def llistat_partides():
    fitxers = []
    for fitxer in os.listdir("../esc"):
        if fitxer.endswith(".esc"):
            fitxers.append(fitxer)
    print(fitxers)

def menu_print():
    sortida("dins menu_print")
    os.system("cls")
    print("-MAIN----------------------------------------------------------------------------------")
    print("1. P. nova")
    print("2. Llistat de P.")
    print("3. Gravar P.")
    print("4. Recuperar P.")    
    print("0. Sortir")
    print(" ")

def menu():
    sortida("dins menu")
    while True:
        sortida("dins menu while")
        menu_print()
        opcio = input("Tria una opció: ")
        if opcio == "1":
            partida_principal = Partida("nom de la partida", "1" )
        elif opcio == "2":
            llistat_partides()
        elif opcio == "3":
            print("Gravar P.")
        elif opcio == "4":
            print("Recuperar P.")
        elif opcio == "0":
            break
        else:
            print("Opció incorrecta")
        input("Prem <ENTER>")



def main():
    sortida("dins main")
    menu();    
    print("a10")
    sortida("a10")


if __name__ == "__main__":
    main()