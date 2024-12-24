import numpy as np
n = 0;

f = open("input.txt", "r")
for x in f:
    p = []
    l = np.array(x.replace("\n","").split(" "))
    for x in l:
        p.append(int(x))
    d = np.diff(p)
    
    if max(abs(d)) <= 3 and min(abs(d)) >= 1:
        if abs(sum(d)) == sum(abs(d)):
            print(d)
            n+=1

print(n)
f.close()