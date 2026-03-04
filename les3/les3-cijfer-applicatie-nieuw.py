
menu_keuze = 0

while menu_keuze !=5:
    studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2), ("Diana", 9.1)]

    menu = ('''
    MENU
    
    Optie 1: Print beschrijvende informatie, waaronder een lijst met studenten en scores, gemiddelde score en de hoogste score.
    Optie 2: Voeg studenten en cijfers toe
    Optie 3: Zoek het cijfer van een student op
    Optie 4: Sorteer de cijfers
    Optie 5: Quit program
    ''')
    print(menu)
    menu_keuze = int(input("Wat wil je doen?: "))

    som_van_cijfers = 0
    hoogste_score = 0
    beste_student = ''

    match menu_keuze:
        case 1:
            print(f'Studenten en hun cijfers:')
            for student, cijfer in studenten:
                print(f'{student} - {cijfer}')
                som_van_cijfers += cijfer

                if cijfer > hoogste_score:
                    hoogste_score = cijfer
                    beste_student = student

            gemiddelde_cijfer = round(som_van_cijfers / len(studenten), 1)
            print(f'\nGemiddelde score: {gemiddelde_cijfer}')
            print(f'De beste student is {beste_student} met een {hoogste_score}!')

    # BONUS
        case 2: # toevoegen studenten en cijfers
            nieuwe_student = input("Wat is de naam van de student?: ").capitalize()
            nieuw_cijfer = float(input("Wat is het cijfer van de student?: "))
            studenten.append((nieuwe_student, nieuw_cijfer))


    #print(studenten)
    #------------------
        case 3: # cijfer van student opzoeken
            opzoeken_input = input('Van welke student wil je het cijfer opzoeken?: ').capitalize()

            studenten_dict = dict(studenten)
            if opzoeken_input in studenten_dict:
                print(f'{opzoeken_input} heeft het cijfer {studenten_dict[opzoeken_input]} gehaald.')
            else:
                print("Deze student staat niet in de lijst.")

    #--------
        case 4: # cijfers sorteren
            gesorteerd = sorted(studenten, key= lambda tup: tup[1])
            for student, cijfer in gesorteerd:
                print(f'{student} - {cijfer}')

        case 5: # quit program
            print("Quitting program")

        case _: # ongeldige keuze
            print("Deze keuze bestaat niet. Kies een bestaande keuze")

