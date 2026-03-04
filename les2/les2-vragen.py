num1 = 30
num2 = 20
num3 = 10
print(f"Origineel: {num1} - {num2} - {num3}")
if num1 > num2:
    (num1, num2) = (num2, num1)
    print(f"Switch 1: {num1} - {num2} - {num3}")
if num2 > num3:
    num2, num3 = num3, num2
    print(f"Switch 2: {num1} - {num2} - {num3}")
if num1 > num2:
    num1, num2 = num2, num1
    print(f"Switch 3: {num1} - {num2} - {num3}")
print(f"Eindresultaat: {num1} - {num2} - {num3}")


x = 6
if x % 2 == 0:
    print("dit is even")
elif x % 2 == 1:
    print("dit is oneven")
elif x % 3 == 0:
    print("dit is deelbaar door 3")
else:
    print("dit is een float")

tf = ""

if not tf:
    print("dit wordt altijd geprint")


oppervlakte = 350
ruimtes = 4
prijs = 2001

if (prijs < 2000) and (ruimtes > 3) and (oppervlakte > 30):
    print("Dit is interessant")
elif prijs > 2000 and ruimtes > 3 and oppervlakte > 100:
    print("erg dur, maar het overwegen waard vanwege de oppervlakte")
elif prijs > 2000 and ruimtes > 3 and oppervlakte > 30:
    print("dit is te duur")

elif ruimtes < 3 :
    print("Ik heb 12 kinderen, dus dit is te klein")
else:
    print("Check even je gegevens, want er klopt iets niet")

x = 5
match x:
    case 1: print("Maandag")
    case 2: print("Dinsdag")
    case 3: print("Woensdag")
    case 4|5: print("Donderdag")
    case _: print("Andere dag")

# =========================== dungeon ========================
print("welkom in de dungeon. Waar wil je heen?\n Kies een deur:")
keuze=input("Kies blauw, geel of rood\n")

while not(keuze == "blauw" or keuze == "geel" or keuze == "rood"):
    print("Kies een geldig antwoord.")
    keuze = input("Kies blauw, geel of rood\n")

if keuze == "blauw":
    print("Je ziet een meer, ga je door de rode deur of de groene deur?")
    keuze2 = input("Kies groen of rood")
    if keuze2 == "groen":
        print("Er springt een monster uit het water en eet je op!\nJe hebt verloren!")
    else:
        print("Je komt in een rode kamer en ziet de finish. Je opent de deur en je bent weer buiten.")

# =======================
# van docent
print("Welkom in de dungeon. Waar wil je heen? \n Kies een deur:")
keuze = input("Kies blauw, geel of groen\n").lower()
#lower zodat als met hoofdletter intypt dan ook geldig

while not (keuze == "blauw" or keuze == "geel" or keuze == "groen"):
    print("kies een geldig antwoord")
    keuze = input("Kies blauw, geel of groen\n")
#blauwe deur
if keuze == "blauw":
    print("Je ziet een meer, ga je door de rode deur of de grone deur?")
    keuze2 = input("kies groen of rood")
    if keuze2 == "groen":
        print("Er springt een monster uit het water en eet je op!\nJe hebt verloren!")
    else:
        print("Je komt in een rode kamer en ziet de finish. Je open de deur en je bent weer buiten.\nGefeliciteerd!")
# als gele deur, dan daarna rood of groen
#groen is monster - rood is finish
# als rode deur meteen finish