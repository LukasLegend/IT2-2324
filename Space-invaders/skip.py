
from laser import Laser

class Skip:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        self.skip_img = None #Defineres i enten fiende eller spiller
        self.laser_img = None #Defineres i fiende eller spiller
        self.lasere = []
        self.skyte_pause_counter = 0
        
    #Tegner et skip og laseren til skipet
    def tegn(self, vindu):
        vindu.blit(self.skip_img, (self.x, self.y)) #Tegner skipet utifra bildet og x og y verdiene
        for laser in self.lasere:
            laser.tegn(vindu)

    def flytt_lasere(self, laser_fart, objekt):
        self.pause() 
        for laser in self.lasere:
            laser.flytt(laser_fart)
            if laser.av_skjerm(750): #Sjekker om laser er avn skjermen med høyden
                self.lasere.remove(laser)
            elif laser.kollisjon(objekt): #SJkker om en laser kolliderer med et ovjekt
                objekt.health -= 10 #Fjerner health fra objektet (spilleren)
                self.lasere.remove(laser) #Fjerner laseren

    def pause(self):
        if self.skyte_pause_counter >= 30: #Hvis det har gått mer enn ett halvt sekund
            self.skyte_pause_counter = 0 #Gjør timeren til 0.
        elif self.skyte_pause_counter > 0: #Hvis pausen_telleren får en verdi over 0:
            self.skyte_pause_counter += 1 #Begynn å legge til 1 hvert sekund.

    def skyt(self):
        if self.skyte_pause_counter == 0: #Hvis det ikke er en aktiv pause pause
            laser = Laser(self.x, self.y, self.laser_img) #Legg til laser
            self.lasere.append(laser) #Legg til i liste
            self.skyte_pause_counter = 1 #Gi pausen verdi over 0
            

    def hent_bredde(self): # henter bredden til skipet
        return self.skip_img.get_width()
    
    def hent_hoyde(self): # henter høyden til skipet
        return self.skip_img.get_height()
