import os
import sys
from pokemon import Pokemon
import json

def rens_termminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

with open("pokedex.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
pokedex = data

pokemons = []
for pokemon_info in pokedex:
    ny_pokemon = Pokemon(pokemon_info)
    pokemons.append(ny_pokemon)

print("---Velkommen til pokemon fantasy---")

while True:
    rens_termminal()
    print("---Pokemon fantasy---")
    print("1: Vis pokemonoversikt")
    print("2: Vis treneroversikt")
    print("3: Vis trener")
    print("4: Avslutt")
    brukervalg = input(">")
    
    if brukervalg == "1":
        print("pokemonoversikt")
        for pokemon in pokemons:
            print(pokemon)
               
        input("Trykk enter for å gå tilbake til hovedmeny")
    elif brukervalg == "2":
        print("avslutter..")
        break
    else:
        print("Ugyldig input")
        input("Trykk enter for å gå tilbake til hovedmeny")


print("Takk for nå")
