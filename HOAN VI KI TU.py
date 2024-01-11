from itertools import permutations
s=[str(i) for i in input()]
b=permutations(s)
for i in list(b):
    print(*i,sep='')