def er_primtall(tall): #oppretter funksjonen "er_primtall" med variabelen tall
    for i in range(1, tall): #For løkke for alle tall mindre enn variabelen tall, bortsett fra 0 siden det ikke er mulig
        if tall % i == 0: #Sjekker om integer modulo av tall og i blir 0, altså om tall er et primtall:
            return True #Hvis påstanden over er riktig returneres true
    return False #Dersom if påstanden ikke har returnert true, returneres false

