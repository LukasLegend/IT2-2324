import pygame
import os
import random
from spiller import Spiller
from fiende import Fiende
from funksjon import kollisjon

pygame.font.init()

pygame.init()
BREDDE, HOYDE = 750, 750
VINDU = pygame.display.set_mode((BREDDE, HOYDE))
FPS = 60

level = 0
liv = 5

tapte = False
tapte_teller = 0

spiller_fart = 5
spiller = Spiller(300, 630, 100)

laser_fart = 7

fiender = []
antall_finder = 0
fiende_fart = 1.5

#font
main_font = pygame.font.SysFont("comicsans", 50)
tapte_font = pygame.font.SysFont("comicsans", 60)

klokke = pygame.time.Clock()

#bakgrunn
BG = pygame.transform.scale(pygame.image.load(os.path.join("bilder", "background-black.png")), (BREDDE, HOYDE))

#gameloop
run = True
while run:
    #Fyller skjermen med bakgrunn
    VINDU.blit(BG, (0,0))

    #hendelser
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    #Legger til nye fiender hver gang ett nytt level starter.
    if len(fiender) == 0:
        level += 1
        antall_finder += 5
        for i in range(antall_finder):
            fiende = Fiende(random.randrange(50, BREDDE - 100), random.randrange(-1500, -300), random.choice(["red", "blue", "green"]), 100)
            fiender.append(fiende)

    #tapte_teller blir økt med 60 per sekund
    if liv <= 0 or spiller.health <= 0:
            tapte = True
            tapte_teller += 1
    
    #Når det er 3 sekunder siden du tapte, slutter spillet
    if tapte:
        if tapte_teller > FPS * 4:
            quit()
            
    #input tastatur
    
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT] and spiller.x - spiller_fart > 0: #venstre, og hindrer spiller å gå utafor vinduet
        spiller.x -= spiller_fart
    if taster[pygame.K_RIGHT] and spiller.x + spiller_fart + spiller.hent_bredde() < BREDDE: #høyre, og hindrer spiller å gå utafor vinduet
        spiller.x += spiller_fart
    if taster[pygame.K_UP] and spiller.y - spiller_fart > 0: #oppover, og hindrer spiller å gå utafor vinduet
        spiller.y -= spiller_fart
    if taster[pygame.K_DOWN] and spiller.y + spiller_fart + spiller.hent_hoyde() + 15 < HOYDE: #ned, og hindrer spiller å gå utafor vinduet (sørger også for at healthbaren ikke går utafor skjermen)
        spiller.y += spiller_fart
    if taster[pygame.K_SPACE]:
        spiller.skyt()

    #tegn på skjermen her

    #laster inn fonts
    liv_tekst = main_font.render(f"Liv: {liv}", 1, (255,255,255))
    level_tekst = main_font.render(f"Level: {level}", 1, (255,255,255))
    tapte_tekst = tapte_font.render("Du tapte!!", 1, (255, 255, 255))

    #Tegner fiender
    for fiende in fiender:
        fiende.tegn(VINDU)

    #Tegner teksten jeg definerte ovenfor i hver av hjørnene
    VINDU.blit(liv_tekst, (10, 10))
    VINDU.blit(level_tekst, (BREDDE - level_tekst.get_width() - 10, 10))

    #Du tapte!! kommer bare på skjerme om tapte == true
    if tapte:
        VINDU.blit(tapte_tekst, (BREDDE/2, 350))

    spiller.tegn(VINDU) #tegner spiller


    #oppdaterer spill
    
    for fiende in fiender[:]: #Lager kopi av listen, kan hjelpe mot glitches når man bruker normale fiender[] listen
        fiende.flytt(fiende_fart) #Får fienden til å bevege seg
        fiende.flytt_lasere(laser_fart, spiller) #Får fienden sin laser til å flytte seg

        if random.randrange(0, 4*60) == 1: #25 prosent sjanse hvert sekund at en fiende skyter, fordi FPS er 60
            fiende.skyt()

        if kollisjon(fiende, spiller): #Sjekker om det er en kollisjon mellom maskene (pixel nøyaktig av self.img) mellom fiende og spiller
            spiller.health -= 10 #Fjerner health fra spilleren
            fiender.remove(fiende) #Fjerner fienden
           

        if fiende.y + fiende.hent_hoyde() > HOYDE: #Hvis en finde når bunnen: fjern ett liv og fjern fienden
            liv -= 1
            fiender.remove(fiende)

    spiller.flytt_lasere(-laser_fart, fiender) #Flytter laseren til spilleren, med negativ fortegn pga laseren skal oppover
    
    pygame.display.flip() #Oppdaterer spillet hvert sekund

    #60 FPS
    klokke.tick(FPS)


pygame.quit()





