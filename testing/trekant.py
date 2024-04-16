class Trekant:
    def __init__(self, grunnlinje: int, høyde: int) -> None:
        self.grunnlinje = grunnlinje
        self.høyde = høyde

    def areal(self):
        return (self.grunnlinje * self.høyde) / 2
    
if __name__ == "__main__":
    print("Testing")

    min_trekant = Trekant(10,10)
    print(min_trekant.areal())

