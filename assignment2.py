
records = [
["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
["Jana", 94], ["Ziad", 75]
]

# print(records[1][0])
class_journal = {}
def grades(records):
    for i in range(len(records)):
        name = records[i][0]
        grade = records[i][1]
        if name in class_journal:
            class_journal[name].append(grade)
        else:
            class_journal[name]= [grade]

    print(class_journal)

grades(records)

# i didnt realize that we dont have to use a function
#  in the first part until it was noted in the second


highestAV = 0
highestAVst = ""
# highestGR 
# LowestGR 


for n in class_journal:
    #print(n, ": ")
    aver = sum(class_journal[n])/len(class_journal[n])
    if aver > highestAV:
        highestAV = aver
        highestAVst = n

    print(f"{n}: {class_journal[n]}, Average: {aver:.2f} ")
    #print(f"{aver:.2f}")

print(f"Highest Average: {highestAVst} {highestAV}")