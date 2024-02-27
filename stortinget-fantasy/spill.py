import os
import sys
import json
from politiker import Politiker
from fantasiparti import Fantasiparti

def rens_termminal():
    # if sys.platform == "Windows":
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

#1 oppsett
with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"]

politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)

print("---Velkommen til stortinget fantasy---")

print()
print("Du må stifte et parti for å starte spillet")
print("Hva skal partiet ditt hete?")
partinavn = input(">")
print("Hva heter du")
spillernavn = input("> ")
spillerparti = Fantasiparti(partinavn, spillernavn)
print(f"Gratulerer! Det nye patiet {partinavn} ble stiftet med partilederen {spillernavn}")
input("Trykk enter for å starte spillet")

while True:
    rens_termminal()
    print("---Stortinget-fantasy---")
    print("1: Vis politikeroversikt")
    print("2: Mitt parti")
    print("3: Avslutt")
    brukervalg = input(">")
    if brukervalg == "1":
        print("politikeroversikt")
        for politiker in politikere:
            print(politiker)
        input("Trykk enter for å gå tilbake til hovedmeny")
    elif brukervalg == "2":
        print("Mitt parti")
        spillerparti.vis_parti()
        input("Trykk enter for å gå tilbake til hovedmeny")
    elif brukervalg == "3":
        print("avslutter..")
        break
    else:
        print("Ugyldig input")
        input("Trykk enter for å gå tilbake til hovedmeny")

    


print("Takk for nå")
