rightList = []
leftList = []
distances = []

f = open("Day1Input.txt", "r")
for x in f:
    l = x.split("   ")
    rightList.append(l[1].replace("\n",""))
    leftList.append(l[0])
f.close()

rightList.sort()
leftList.sort()

for x in range(len(rightList)):
    distances.append(abs(int(rightList[x])-int(leftList[x])))

print(sum(distances))