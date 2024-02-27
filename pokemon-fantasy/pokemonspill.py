import os
import sys
from pokemon import Pokemon
from trener import Trener
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
    print("2: Lag ny trener")
    print("3: Vis treneroversikt")
    print("4: Vis trener")
    print("5: Avslutt")
    brukervalg = input(">")
    
    if brukervalg == "1":
        print("pokemonoversikt")
        for pokemon in pokemons:
            print(pokemon)
    elif brukervalg == "2":
        print("Hva heter du?")
        brukerinput = input(">")
        pokemon_liste = ["Charizard", "Mewtwo", "Pikachu"]
        trener = Trener(brukerinput, pokemon_liste)
        input("Trykk enter for å gå tilbake til hovedmeny")

    elif brukervalg == "3":
        trener.vis_trener()
        input("Trykk enter for å gå tilbake til hovedmeny")

    elif brukervalg == "5":
        print("avslutter..")
        break
    else:
        print("Ugyldig input")
        input("Trykk enter for å gå tilbake til hovedmeny")


print("Takk for nå")
