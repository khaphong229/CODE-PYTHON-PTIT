from math import *
n=int(input())
hang=[0]*n; cot=[0]*n
ans=0
for i in range(n):
    s=input()
    for j in range(len(s)):
        if s[j]=='C':
            hang[i]+=1
            cot[j]+=1
for i in hang:
    if i>=2: ans+=comb(i,2)
for i in cot:
    if i>=2: ans+=comb(i,2)
print(ans)