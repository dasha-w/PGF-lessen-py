"""
Albatros
Onderstaande code is een puzzel.
De 7 coordinaten vormen een woord van 7 letters.
Ontcijfer elk coordinaat een voor een tot een letter uit de puzzel lijst.
Sla jou ontvijferde letters op in de antwoord variabele.
"""

puzzel = ["Albatros", "poncho", "vlinder", "glitter"]
coordinaten = [(0,0), (2,0), (0,-2), (1,3), (0,3), (2,4), (1,1)]
antwoord = ""

for i,j in coordinaten:
    letter = puzzel[i][j]
    #print(letter)
    antwoord += letter

print(antwoord)