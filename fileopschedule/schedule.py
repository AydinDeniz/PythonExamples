a = input("Please enter filename for the courses list: ")
b = input("Please enter filename for the finals list: ")
id = input("Please enter a student ID: ")
courses = open(a, "r")
finals = open(b,"r")
Lines = courses.readlines()
temp = []
ids = []
crns = []
dic = {}
for i in Lines:
    tempcrns = []
    temp = [x.replace('\n', '') for x in i.split(" ")]
    for j in temp:  # getting rid of useless spaces in courses.txt
        try:
            int(j)
        except ValueError:
            temp.pop()
    if not (temp[0] in ids):
        ids.append(temp[0])

while True:
    if not id in ids:
        print("There is no student with ID {}".format(id))
        id = input("Please enter a student ID: ")
    else:
        break

for i in Lines:
    tempcrns = []
    temp = [x.replace('\n', '') for x in i.split(" ")]
    for j in temp:  # getting rid of useless spaces in courses.txt
        try:
            int(j)
        except ValueError:
            temp.pop()
    if not (temp[0] in ids):
        ids.append(temp[0])
    for k in range(1,len(temp)):
        tempcrns.append(temp[k])
    if temp[0] == id:
        crns += tempcrns

print("Final exam schedule of student with ID {}".format(id))
withoutfinal = crns.copy()
Lines = finals.readlines()
for j in crns:
    for i in Lines:
        templist = [x for x in i.split("\t")]
        if j == templist[0]:
            temp = [x.replace('\n', '') for x in i.split("\t")]
            temp.pop(0)
            strtemp = temp[0]+"\t"+temp[1]+" "+temp[2]
            saylist1 = [x for x in  temp[1].split(".")]
            saylist2 = [x for x in  temp[2].split(":")]
            str2 = ""
            for i in saylist2:
                str2 += i
            saylist2 = [x for x in str2.split("-")]
            time = int(saylist1[0]) * 365 * 24 + int(saylist1[1]) * 30 * 24 + int(saylist1[2]) * 24 + int(saylist2[0]) / 100
            dic[time] = strtemp
            withoutfinal.remove(templist[0])
dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[0])}
for i in dic.values():
    print(i)

print("Courses without a final exam:",', '.join(map(str, withoutfinal)))
courses.close()
finals.close()