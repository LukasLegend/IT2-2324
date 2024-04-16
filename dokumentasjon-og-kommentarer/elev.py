class Elev:

    """
    En klasse for elever på VGS

    Attributter
        navn (str) ? = navnet til eleven
        alder (int) = alder til eleven
        klasse (str) = klassen til eleven
        fag (list(str)) = liste med fagene til eleven

    Metoder
        legg_til_fag(str, fag) = legger til fag i listen
        fjern_fag(str, fag) = fjerner fag fra listen med fag
        vis_info(self) = viser informasjon om elev

    """
    def __init__(self, navn: str, alder: str, klasse: str) -> None:
        self.navn: str = navn
        self.alder: int = alder
        self.klasse: str = klasse
        self.fag: list[str] = []

    def legg_til_fag(self, fag: str):
        self.fag.append(fag)
    
    def fjern_fag(self, fag: str):
        self.fag.remove(fag)
    
    def vis_info(self):
        print(f"{self.navn} ({self.alder})")

