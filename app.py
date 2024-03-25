import subprocess
import os

Starting_PATH = "katalog Startowy"
current_path = Starting_PATH

def pokaz_pliki(typ_pliku):
    lista = os.listdir()
    for sciezka in lista:
        if os.path.isdir(sciezka) and typ_pliku == "k":
            print(sciezka + " k")

        elif os.path.isfile(sciezka) and typ_pliku == "p":
            print(sciezka + " p")
        
        elif typ_pliku == "a":
            if os.path.isdir(sciezka):
                print(sciezka + " k")
            elif os.path.isfile(sciezka):
                print(sciezka + " p")



while True:
    try:
        zapytanie = input(": ")
        if zapytanie.lower() == "exit":
            break

        elif zapytanie.startswith("cd "):
            nowy_katalog = zapytanie[3:]
            if os.path.exists(nowy_katalog):
                os.chdir(nowy_katalog)
                current_path = os.path.abspath(nowy_katalog)
                print(current_path)

            else:
                print("nie ma takiego katalogu!")
        elif zapytanie == "dir":
                wybor = input("katalogi(k),pliki(p), wszystko(a): ")
                pokaz_pliki(wybor)
        else:
            wynik = subprocess.run(zapytanie, capture_output=True, text=True, cwd=current_path )
            print(wynik.stdout)
    except Exception as wyj:
            print("Blad ", wyj)