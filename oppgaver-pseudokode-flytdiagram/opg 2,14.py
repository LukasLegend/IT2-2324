#OPPGAVE 1

#Programmet ender opp med nummer C, 5, 2, 6, 8, 12 fordi den går bare gjennom tallene i listen en gang

#OPPGAVE 2 

#Under er den utvidede psuedokoden

#SET i TO 0
#For i in range 10   
     #FOR hver i LESSER THAN n - 1
         # IF a[i] GREATER THAN a[i+1]    
        # CALL byttPlass()
     #ENDIF
     #ENDFOR
#ENDFOR


#Med denne for løkken, kjøres koden på nytt 10 ganger som sikrer at den endelige listen faktisk er listen i stigende rekkefølge

def byttplass(list, a,b):
    list[a], list[b] = list[b], list[a]
    return list

i = 0
a = [8, 5, 2, 6, 12]
for i in range(10):
    for i in range(4):
        if a[i] > a[i+1]:
            byttplass(a, i, i+1)

print(a)








    
