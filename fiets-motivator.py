# De fiets-motivator


# Geef aan welk weer het is
keuze = input ("Wat is het weer? \n Kies uit zon, regen of anders : ")

while not (keuze == "zon" or keuze == "regen" or keuze == "anders") :
    print("Je hebt geen correcte keuze gemaakt")
    keuze = input("Wat is het weer? \n Kies uit zon, regen of anders : ")

# De opties als de zon schijnt
if keuze == "zon" :
    print("Het is lekker weer!")
    keuze2 = input("Pak je de fiets of de auto? ")
    if keuze2 == "fiets" :
        print("Goed bezig! Je werkt aan je gezondheid")
    elif keuze2 == "auto" :
        print("Je hebt Frans Timmermans boos gemaakt")
