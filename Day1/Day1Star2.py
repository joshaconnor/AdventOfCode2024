rightList = []
leftList = []
similarities = []

f = open("Day1Input.txt", "r")
for x in f:
    l = x.split("   ")
    rightList.append(l[1].replace("\n",""))
    leftList.append(l[0])
f.close()

for x in leftList:
    similarities.append(rightList.count(x)*int(x))

print(sum(similarities))