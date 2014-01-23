num = int(input("Please enter the number of students: "))

i = 1
name_list = []
score_list = []
highest1 = 0
highest2 = 0

while i<=num:
    name_list.append(input("Please enter the name of a student: "))
    score_list.append(int(input("Please enter the score of that student: ")))
    i += 1

for score in score_list:
    if score >= highest1:
        highest1 = score

name1 = name_list[score_list.index(highest1)]
score_list.remove(highest1)
name_list.remove(name1)

for score in score_list:
    if score >= highest2:
        highest2 = score

name2 = name_list[score_list.index(highest2)]

print(name1)
print(name2)
