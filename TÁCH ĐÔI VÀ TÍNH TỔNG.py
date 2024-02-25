def solve(n,left,right):
    length=len(n)
    mid=(left+right)//2
    before=n[:mid]
    after=n[mid:]
    trc=''
    sau=''
    for i in before:
        trc+=i
    for j in after:
        sau+=j
    return int(trc)+int(sau)

n=input()
while len(n)!=1:
    a=[i for i in n]
    n=str(solve(a,0,len(a)))
    print(n)