import os
import sys
from politiker import Politiker
import json

def rens_termminal():
    if sys.platform == "Windows":
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

while True:
    rens_termminal()
    print("---Stortinget-fantasy---")
    print("1: Vis politikeroversikt")
    print("2: Avslutt")
    brukervalg = input(">")
    if brukervalg == "1":
        print("politikeroversikt")
        for politiker in politikere:
            print(politiker)
        input("Trykk enter for å gå tilbake til hovedmeny")
    elif brukervalg == "2":
        print("avslutter..")
        break
    else:
        print("Ugyldig input")
        input("Trykk enter for å gå tilbake til hovedmeny")

    


print("Takk for nå")
