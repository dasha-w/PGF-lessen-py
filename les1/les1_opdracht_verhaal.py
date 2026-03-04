print("Je gaat nu een verhaal genereren. Beantwoord de vragen met 1 woord (excl. lidwoorden).")

jouw_naam = input("Vul je naam in: ")
naam_vriend = input("Wat is de naam van je vriend?: ")
locatie = input("Maak de zin af: Jullie wandelen in... ")
voorwerp = input("Welke tool gebruik je het liefst in de keuken?: ")
#weer = input("Wat zijn de weersomstandigheden?: ")
angst = input("Waar ben je bang voor?: ")


print(f'Mijn naam is {jouw_naam} en samen met mijn vriend {naam_vriend} wandelen we in {locatie}.\n'
      f'Daar vinden we een vreemd voorwerp, namelijk {voorwerp}.\n'
      f'Ondanks mijn angst voor {angst}, wordt het onverwacht het begin wordt van een grappig en onvergetelijk avontuur.'
      )
