while True:                                            # Dine kommentarer her
    try:                                               #  tester
        alder = int(input("Hvor gammel er du? "))      #  alder input fra brukeren
        break                                          #  bryter løkken
    except:                                            #  printes hvis behovene ovenfor ikke møtes
        print("Ugyldig input. Alder må være et tall.") #
år = 2024                                              # 2024 - år
fødselsår = år - alder                                 # regner ut fødselsår
print(f"Du er født i {fødselsår}")                     # printer fødselsår