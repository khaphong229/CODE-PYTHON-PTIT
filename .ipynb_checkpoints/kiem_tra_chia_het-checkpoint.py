def solve(l,r,n):
    dem=0
    for i in range(l,r+1):
        check=False
        for j in range(2,n+1):
            if i%j==0:
                check=True
                break
        if not check:
            dem+=1
    return dem
while True:
    user_input=input().split()
    if len(user_input)<2:
        break
    l,r=map(int,user_input)
    n=int(input())
    print(solve(l,r,n))