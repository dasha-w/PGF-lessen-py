from prettytable import PrettyTable
table = PrettyTable()
print(table)

'''make table, delete, filter, sort, colour'''

# add by rows (kan ook 1 row
table.field_names = ["City name", "Area", "Population"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259],
        ["Brisbane", 5905, 1857594],
        ["Darwin", 112, 120900],
        ["Hobart", 1357, 205556],
        ["Sydney", 2058, 4336374],
        ["Melbourne", 1566, 3806092],
    ]
)
print(table)

# add 1 row
table.add_row(["Perth", 5386, 1554769])

print(table)

#add 1 column
table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])


print(table)

# delete a row & column
#table.del_row(0)
#print(table)

#table.del_column('Annual Rainfall')
#print(table)
# filter display table

print(table.get_string(fields=["City name", "Population"]))
print(table.get_string(start=1, end=4))

# alignment
table.align = 'r'
print(table)

table.align["City name"] = "l"
table.align["Area"] = "c"
table.align["Population"] = "r"
table.align["Annual Rainfall"] = "c"
print(table)
# sorteren
print(table.get_string(sortby="Population"))

# kleuren
from prettytable.colortable import ColorTable, Themes

table = ColorTable(theme=Themes.OCEAN)
'''
table.field_names = ["City name", "Area", "Population"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259],
        ["Brisbane", 5905, 1857594],
        ["Darwin", 112, 120900],
        ["Hobart", 1357, 205556],
        ["Sydney", 2058, 4336374],
        ["Melbourne", 1566, 3806092],
    ]
)
''
print(table)