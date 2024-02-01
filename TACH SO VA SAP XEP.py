def get_num(n):
    b=[]
    res=''
    for i in n:
        if i.isalpha():
            res+=' '
        else:
            res+=i
    for i in res.split():
        i=int(i)
        b.append(i)
    return b

n=int(input())
ans = []
for _ in range(n):
    s=input()
    ans+=get_num(s)
ans.sort()
for i in ans:
    print(i)