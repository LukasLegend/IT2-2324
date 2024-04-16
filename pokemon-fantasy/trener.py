from pokemon import Pokemon

class Trener:
    def __init__(self, navn: str, pokemons: list) -> None:
        self.navn = navn
        self.pokemons = pokemons

    def __str__(self) -> str:
        return f"{self.navn} Pokemons: {self.pokemons}"
    
    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
        else:
            print("feil")

    def remove_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)
        else:
            print("feil")
    
    def vis_trener(self):
        print(f"-- {self.navn} --")
        print("Pokemon:")
        for pokemon in self.pokemons:
            print(pokemon)
        print() #Tom linje        



