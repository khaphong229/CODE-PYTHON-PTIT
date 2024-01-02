def sum(n):
    sum=0
    length=len(str(n))
    for i in range(0,length,2):
        sum+=int(str(n)[i])
    return sum
def check(n):
    length=len(str(n))
    for i in range(1,length,2):
        if int(str(n)[i])!=0:
            return False
    return True
def multi(n):
    temp=1
    length=len(str(n))
    kiem_tra=check(n)
    for i in range(1,length,2):
        if kiem_tra:
            temp=0
        else:
            if int(str(n)[i])==0:
                continue
            temp*=int(str(n)[i])
    return temp

n=int(input())
for _ in range(n):
    num=input()
    print(sum(num),multi(num),sep=' ')