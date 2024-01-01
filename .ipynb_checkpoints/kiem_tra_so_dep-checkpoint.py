def check(n):
    if len(set(str(n)))>=3:
        return False
    for x in range(2,len(str(n))):
        if str(n)[x]!=str(n)[x-2]:
            return False
    return True
if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        print('YES') if check(num) else print('NO')