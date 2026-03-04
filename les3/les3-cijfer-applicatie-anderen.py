# Mick
studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2), ("Diana", 9.1)]
total = 0
highest_student_grade = []
prev_student_grade = 0

print("Studenten en hun cijfers:")
for name, grade in studenten:
    total += grade
    print(name, grade)

    if prev_student_grade < grade:
        highest_student_grade.insert(0, name)
        highest_student_grade.insert(1, grade)
    prev_student_grade = grade

average = round(total / len(studenten), 1)
print(f"\nGemiddelde score: {average}")
print(f"De beste student is {highest_student_grade[0]} met een {highest_student_grade[1]}!")

#Bart
studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2), ("Diana",9.2)]
totaal = 0
hoogste_naam = studenten[0][0]
hoogste_cijfer = studenten[0][1]
for naam, cijfer in studenten:
    print(f" {naam} : {cijfer}")
    totaal += cijfer
    if cijfer > hoogste_cijfer:
        hoogste_cijfer= cijfer
        hoogste_naam= naam
gemiddelde = round(totaal/ len(studenten), 1)
print(f"Het gemiddelde cijfer is {gemiddelde}")
print(f"De student met het hoogste cijfer is {hoogste_naam} met een {hoogste_cijfer}.")