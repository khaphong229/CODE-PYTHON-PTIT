def tinh(n):
    tich=1
    tong=0
    length=len(str(n))
    for i in range(length):
        if i%2==0:
            if int(str(n)[i])==0:
                continue
            else:
                tich*=int(str(n)[i])
        else:
            tong+=int(str(n)[i])
    return tich, tong

n=int(input())
for _ in range(n):
    num=int(input())
    result=tinh(num)
    print(result[0],result[1],sep=' ')