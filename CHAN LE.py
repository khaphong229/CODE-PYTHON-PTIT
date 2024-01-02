def sum(n):
    total=0
    while n!=0:
        total+=n%10
        n//=10
    return total%10==0

def check(n):
    str_n=str(n)
    length=len(str_n)
    for i in range(length-1):
        if abs(int(str_n[i+1])-int(str_n[i]))!=2:
            return False
    return True

if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        print('YES') if sum(num) and check(n) else print('NO')