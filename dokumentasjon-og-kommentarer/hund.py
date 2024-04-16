class Hund:

    """
    En klasse for en hund og egenskaper den har

    Attributter:
        navn (str) = navnet til hunden
        alder (int) = alder til hunden
        rase (str) = rasen til hunden

    Metoder:

        bjeff(self) = får hunden til å bjeffe
        Viftpahalen(self) = får hund til å vifte på halen 
        info(self) = viser informasjon
    """
    def __init__(self, navn, alder, rase):
        self.navn = navn
        self.alder = alder
        self.rase = rase
 
    def bjeff(self):
        return f"{self.navn} sier: Woof!"
 
    def viftPaaHalen(self):
        return f"{self.navn} vifter på halen!"
 
    def info(self):
        return f"{self.navn} er en {self.alder} år gammel {self.rase}."
 
 
# Test av klassen
if __name__ == "__main__":
    min_hund = Hund("Rex", 5, "Schäfer")
    print(min_hund.bjeff())
    print(min_hund.viftPaaHalen())
    print(min_hund.info())