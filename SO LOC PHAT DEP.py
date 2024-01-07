def check1(n):
    a=[int(i) for i in n]
    for i in a:
        if i!=6 and i!=8:
            return False
    return True
def check2(n):
    a=[int(i) for i in n]
    for i in range(len(a)):
        if a[0]==8:
            return False
        if a[i]==8 and a[i-1]!=6 and a[i-1]!=8:
            return False
        if i>1 and a[i]==8 and a[i-1]==8 and a[i-2]!=6:
            return False
    return True

n=input()
print('YES') if check1(n) and check2(n) else print('NO')