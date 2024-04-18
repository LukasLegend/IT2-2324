import pygame
from spillobjekt import Spillobjekt

class Spillbrett:
    def __init__(self, bredde, hoyde) -> None:
        self.hoyde: int = hoyde
        self.bredde: int = bredde
        self.objekter: list[Spillobjekt] = []

        #alle "ting" i pygame må ha en surface og en rect
        self.surface = pygame.Surface((self.bredde, self.hoyde))
        self.rect = self.surface.get_rect()

        self.rect.topleft = [0,0]

        self.surface.fill("green")

    def legg_til_objekt(self, nytt_objekt: Spillobjekt):
        self.objekter.append(nytt_objekt)

    def fjern_objekt(self, objekt: Spillobjekt):
        self.objekter.remove(objekt)

    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.surface, self.rect)