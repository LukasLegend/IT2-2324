class Pokemon:
    def __init__(self, pokemon_info) -> None:
        self.navn = pokemon_info["name"]["english"]
        self.type = pokemon_info["type"]
        self.base = pokemon_info["base"]


    def __str__(self):
        return f"{self.navn}, Type: {self.type} Stats: {self.base}"