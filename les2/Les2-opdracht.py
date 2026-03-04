print("Goeiemorgen!\n Het is 8 uur\nVandaag is een drukke dag en je moet naar je werk.\n"
      "Waat doe je als eerst?")
keuze = input("Kies opstaan of snoozen\n").lower()

while not (keuze == "opstaan" or keuze == "snoozen"):
    print("Dit is geen optie. Wat doe je?\n")
    keuze = input("Kies opstaan of snoozen\n").lower()
'''
if keuze == "snoozen":
    print("O nee, het is 10.15! Je komt te laat op werk")
'''

if keuze == "opstaan":
    print("Je staat op.\nWat doe je nu?\n")
    keuze_2 = input("Kies uit douchen, de hond uit laten of ontbijten:\n").lower()

    if keuze_2 == "douchen":
        print("je doucht je ruikt lekker, maar je hebt geen tijd meer om te eten.\nJe komt zo te laat.\nWat doe je nu?\n")
        keuze_3 = input("Kies om toch te eten, of je naar je werk te gaan.").lower()

        if keuze_3 == "werk":
            print("Je komt op tijd op je werk, maar je hebt heel de dag honger dus je presteert niet zo goed.")
        elif keuze_3 == "eten":
            print("Je komt te laat op je werk, je baas is boos, je bent ontslagen.")
        else:
            print("Dit is geen juiste keuze")
#    if keuze_2 ==
else:
    print("Je valt weer in slaap, je wordt wakker om 10 uur.\nJe bent te laat op je werk, je bent helaas ontslagen.")
