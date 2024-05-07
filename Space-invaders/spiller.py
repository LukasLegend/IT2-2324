from skip import Skip
import pygame
import os

class Spiller(Skip):
    def __init__(self, x, y, health):
        super().__init__(x, y, health)
        self.skip_img = pygame.image.load(os.path.join("bilder", "pixel_ship_yellow.png"))
        self.laser_img = pygame.image.load(os.path.join("bilder", "pixel_laser_yellow.png"))
        self.mask = pygame.mask.from_surface(self.skip_img) # Lag en mask, mer nøyaktig enn rect men så og si samme funksjon
        self.maks_health = health

    def flytt_lasere(self, laser_fart, objekter):
        self.pause() #Sjekker om det er en verdi over 0 på pause counter altså om spiller ikke kan skyte
        for laser in self.lasere:
            laser.flytt(laser_fart) #Flytter laser med farten fra variabel "laser_fart"
            if laser.av_skjerm(750): #Sjekker om laseren er av skjermen med høyden av vinduet, 750
                self.lasere.remove(laser) #Fjerner
            else:
                for objekt in objekter:
                    if laser.kollisjon(objekt): #Sjekker om en laser kolliderer med et objekt
                        objekter.remove(objekt) #Fjerner objektet
                        self.lasere.remove(laser) #Fjerner laseren

    def tegn(self, vindu):
        super().tegn(vindu) #tar tegn funksjonen fra skip.py. Super tar fra "skip" klassen som spiller arver fra
        self.healthbar(vindu) #tegner healthbaren
        
    def healthbar(self, vindu):
        pygame.draw.rect(vindu, (255,0,0), (self.x, self.y + self.hent_hoyde() + 10, self.hent_bredde(), 10)) #Sørger for at healthbaren er under skipet.
        pygame.draw.rect(vindu, (0,255,0), (self.x, self.y + self.hent_hoyde() + 10, self.hent_bredde() *  (self.health/self.maks_health), 10))
        