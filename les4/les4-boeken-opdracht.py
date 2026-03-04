groep1 = ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit" , "De Da Vinci Code" ,
"Twilight" , "De Vijfde Golf" , "Harry Potter", "De Hobbit"]

groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight", "The Hunger Games" , "Gone Girl" ,
"Twilight", "De Hobbit"]

# vraag 1
set1 = set(groep1)
set2 = set(groep2)

#print unieke boeken voor beide groepen
print(f'De unieke boeken voor groep 1 zijn: \n{set1}')
print(f'De unieke boeken voor groep 2 zijn: \n{set2}')

# Vraag 2
print(f'\n')
print(f'De boeken die door beide groepen zijn geleend zijn: \n{set1 & set2}')

# Vraag 3
print(f'\n')
print(f'Boeken die door groep 1 zijn geleend en niet door groep 2 zijn: \n{set1-set2}')
print(f'Boeken die door groep 2 zijn geleend en niet door groep 1 zijn: \n{set2-set1}')

# Vraag 4
print(f'\n')
dict1 = {}
for boek in groep1:
    if boek in dict1:
        dict1[boek] += 1
    else:
        dict1[boek] = 1
print(dict1)

dict2 = {}
for boek in groep2:
    if boek in dict2:
        dict2[boek] += 1
    else:
        dict2[boek] = 1
print(dict2)

# Vraag5

print(max(dict1.values()))
print(max(dict1, key=dict1.get, default=None))