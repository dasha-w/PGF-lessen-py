studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2), ("Diana", 9.1)]

print(f'Studenten en hun cijfers:')
for student, cijfer in studenten:
    print(f'{student} - {cijfer}')

#-------------------------------------------
print(f'')

som_van_cijfers= 0
aantal_studenten = 0

for student, cijfer in studenten:
    som_van_cijfers += cijfer
    aantal_studenten += 1

gemiddelde_score = som_van_cijfers / aantal_studenten
print(f'Gemiddelde score: {gemiddelde_score}')

#-------------------------------------------
print(f'')

hoogste_score = 0
beste_student = ''

for student, cijfer in studenten:
    if cijfer > hoogste_score:
        hoogste_score = cijfer
        beste_student = student

print(f'De beste student is {beste_student} met een {hoogste_score}!')
#-------------------------------------------
print(f'')

nieuwe_input = input(f'Wil je een student en cijfer toevoegen? Ja of Nee: ').lower()

if nieuwe_input == "ja":
     nieuwe_student = input("Wat is de naam van de student? ").capitalize()
     nieuw_cijfer = float(input("Wat is het cijfer van de student? "))
     studenten.append((nieuwe_student, nieuw_cijfer))

print(studenten)
#-------------------------------------------
print(f'')

opzoeken_input = input('Wil je een student opzoeken? Ja of Nee: ').lower()

if opzoeken_input == "ja":
    student_opzoeken = input("Voor welke student wil je het cijfer opzoeken?: ").capitalize()
    for student, cijfer in studenten:
        if student == student_opzoeken:
            print(f'Het cijfer van {student_opzoeken} is {cijfer}.')

#-------------------------------------------
print(f'')

sorteer_lijst = []
for student, cijfer in studenten:
    sorteer_lijst.append(cijfer)

sorteer_lijst.sort()
print(f'De gesorteerde cijferlijst is {sorteer_lijst}')