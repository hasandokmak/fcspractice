
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



new_grades = [["Jana", 99], ["Ziad", 78], ["Layla", 84]]

for name, grade in new_grades:
    if name in class_journal:
        class_journal[name].append(grade)
    else:
        class_journal[name] = [grade]
highestAV = 0
highestAVst = ""
# highestGR 
# LowestGR 
mindiff = float('inf')
mcSTUDENT = ""

belowSeventy = []

totalg = 0

ttt =0
count =0

for n in class_journal:
    #print(n, ": ")
    aver = sum(class_journal[n])/len(class_journal[n])
    if aver > highestAV:
        highestAV = aver
        highestAVst = n

    diff = max(class_journal[n]) - min(class_journal[n])
    if diff < mindiff:
        mindiff = diff
        mcSTUDENT = n

    for gr in class_journal[n]:
        if gr<70:
            belowSeventy.append(n)
            break

    for gr in class_journal[n]:
        totalg+=1
        ttt += gr

    print(f"{n}: {class_journal[n]}, Average: {aver:.2f} ")
    #print(f"{aver:.2f}")

print(f"Highest Average: {highestAVst} {highestAV}")
print(f"Most Consistent Student: {mcSTUDENT} with lowest difference {mindiff}")
print(f"Student who have grades below 70: {belowSeventy}")
print(f"Total Grades: {totalg}")
classav = ttt/totalg
print(f"Overall Average: {classav}")




with open("classfile.txt", "w") as f:
    f.write(f"Highest Average: {highestAVst} {highestAV}\n")
    f.write(f"Most Consistent Student: {mcSTUDENT} with lowest difference {mindiff}\n")
    f.write(f"Student who have grades below 70: {belowSeventy}\n")
    f.write(f"Total Grades: {totalg}\n")
    f.write(f"Overall Average: {classav}\n")