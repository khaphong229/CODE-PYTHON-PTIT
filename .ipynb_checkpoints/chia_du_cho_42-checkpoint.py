from sys import stdin
a=[]
for s in stdin:
    a+=list(map(int,s.split()))
unique_num=set()
for x in a:
    if x%42==1:
        unique_num.add(x)
print(len(unique_num))