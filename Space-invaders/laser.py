import pygame
from funksjon import kollisjon

class Laser:
    def __init__(self, x, y, img) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img) # Lag en mask, mer nøyaktig enn rect men så og si samme funksjon

    #tegner laseren
    def tegn(self, vindu):
        vindu.blit(self.img, (self.x, self.y))

    #Beveger laseren
    def flytt(self, fart):
        self.y += fart

    #Sjekker om laseren er av skjermen, returnerer true eller false. Putter "not" foran fordi jeg vil ha true hvis den er av skjermen
    def av_skjerm(self, hoyde):
        return not(self.y <= hoyde and self.y >= 0)
    
    #sjekker om det er kollisjon mellom laser og objekt
    def kollisjon(self, objekt):
        return kollisjon(self, objekt)