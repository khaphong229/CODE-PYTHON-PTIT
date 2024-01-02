def ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        a=int(input())
        b=int(input())
        print(ucln(a,b))