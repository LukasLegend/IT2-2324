class Figur:
    def __init__(self,x: int,y:int) -> None:
        self.x: int = x
        self.y: int = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
        
class Trekant(Figur):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

if __name__ =="__main__":
    print("Testing")

    min_figur = Figur(10,20)
    print(min_figur)