def check(n):
    if str(n)!=str(n)[::-1]:
        return False
    if len(str(n))%2!=0:
        return False
    for i in str(n):
        if int(i)%2!=0:
            return False
    return True

for _ in range(int(input())):
    n=int(input())
    for i in range(22,n):
        if check(i):
            print(i,end=' ')
    print()