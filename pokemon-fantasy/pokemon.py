class Pokemon:
    def __init__(self, pokemon_info) -> None:
        self.navn = pokemon_info["name"]["english"]
        self.type = [type["type"] for type in pokemon_info["type"]]
        self.base = pokemon_info["base"]


    def __str__(self):
        return f"{self.navn} {self.type} {self.base}"