
records = [
["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
["Jana", 94], ["Ziad", 75]
]

# print(records[1][0])
d = {}
def grades(records):
    for i in range(len(records)):
        name = records[i][0]
        grade = records[i][1]
        if name in d:
            d[name].append(grade)
        else:
            d[name]= [grade]

    print(d)

grades(records)
