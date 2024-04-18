import pygame

class Spillobjekt:
    def __init__(self, farge: str) -> None:
        self.surface = pygame.Surface((50,50)) # lager pygame surface som er 50px gredt og 50px høyt
        self.rect = self.surface.get_rect()# lager rect som ligger rundt surface-en
        self.surface.fill(farge)

    def plassering(self, x: int, y: int):
        self.rect.center = (x,y)

    def flytt(self, dx: int, dy: int):
        self.rect.move_ip(dx, dy)

