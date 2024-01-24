##Eksempel penger tjent på Spotify

# Algoritme som regner ut hvor mye penger vi tjener på Spotify

# -Psuedo naturlig språk

# Hent inn antall streams
# Hvis antall streams er større enn 30 000 000
#     Returnerer antall streams ganger 70% (0.7)
# Ellers hvis antall streams er større enn 1 400 000:
#     Returnerer antall streams ganger 40% (0.4)
# Ellers:
#     Returnerer 0

# - Psudeokode etter udir standard

# SET antall_streams to READ "hvor mange streams?"
# IF antall_streams GREATER THAN 30 000 000
#   Then DISPLAY ANTALL STREAMS*0,7
#ELSE IF antall_streams GREATER THAN 1 400 000
#   Return antall streams gange *0,4
#Ellers:
#   Return 0

# -Python:

antall_streams = input("Hvor mange streams?")
if antall_streams > 30_000_000:
    print(antall_streams * 0.7)
elif antall_streams > 1_400_000:
    print(antall_streams * 0.4)
else:
    print(0)