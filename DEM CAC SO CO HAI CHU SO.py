n=input()
d=dict({})
for i in range(0,len(n)-1,2):
    if n[i:(i+2)] in d:
        d[n[i:(i+2)]]+=1
    else:
        d[n[i:(i+2)]]=1
for i,j in d.items():
    print(i,j)