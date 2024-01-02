def ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def check_ucln(a,b):
    return ucln(a,b)==1

def solve(l,r):
    list=[]
    for a in range(l,r-1):
        for b in range(a+1,r):
            for c in range(b+1,r+1):
                if c<=r and check_ucln(a,b) and check_ucln(b,c) and check_ucln(a,c):
                    list.append((a,b,c))
    return list
if __name__=='__main__':
    l,r=map(int,input().split())
    result=solve(l,r)
    for x in result:
        print(x)
        