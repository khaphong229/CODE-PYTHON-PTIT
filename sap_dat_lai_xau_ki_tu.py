def check(s1,s2):
    if len(s1)!=len(s2):
        return False
    a=dict({})
    for x in s1:
        if x in a:
            a[x]+=1
        else: a[x]=1
    b=dict({})
    for x in s2:
        if x in b:
            b[x]+=1
        else: b[x]=1
    for i in a:
        if i not in b:
            return False
        if a[i]!=b[i]:
            return False
    return True
    

if __name__=='__main__':
    t=int(input())
    for _ in range(1,t+1):
        s1=input()
        s2=input()
        print(f'Test {_}: YES') if check(s1,s2) else print(f'Test {_}: NO')