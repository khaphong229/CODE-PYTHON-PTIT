def check(n):
    str_n=str(n)
    if len(str_n)%2==0:
        return False
    if str_n[0]==str_n[1]:
        return False
    for i in range(0,len(str_n)-2,2):
        if str_n[i]!=str_n[i+2]:
            if str_n[i]!=str_n[-1]:
                return False
    return True

t=int(input())
for _ in range(t):
    n=input()
    print('YES') if check(n) else print('NO')