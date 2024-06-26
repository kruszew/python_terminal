import subprocess
import os
import magic

Starting_PATH = "Katalog Startowy"
current_path = Starting_PATH
magic_detect = magic.Magic()
os.chdir(Starting_PATH)

def sprawdz_typ(plik, typ):
    if typ.lower() == "t":
        file_type = magic_detect.from_file(plik)
        return file_type
    else:
        return ""
        

def pokaz_pliki(typ_pliku):
    lista = os.listdir()
    typ =input("pokazać typ plików?(t/n): ")
    for sciezka in lista:
        try:
            if os.path.isdir(sciezka) and typ_pliku == "k":
                print(sciezka + " k ")
                
            elif os.path.isfile(sciezka) and typ_pliku == "p":
                print(sciezka + " p " + sprawdz_typ(sciezka, typ))
            
            elif typ_pliku == "a":
                if os.path.isdir(sciezka) :
                    print(sciezka + " k ")
                elif os.path.isfile(sciezka):
                    print(sciezka + " p " + sprawdz_typ(sciezka, typ))
        except Exception as e:
            print("Błąd podczas przetwarzania pliku:", e)

def terminal():
    global current_path
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
                
def wyswietl_menu():
    print("=== MENU ===")
    print("1. Terminal")
    print("2. Wyjście")

while True:
    wyswietl_menu()
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        terminal()
    elif wybor == "2":
        print("Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór. Wybierz opcję od 1 do 2.")
