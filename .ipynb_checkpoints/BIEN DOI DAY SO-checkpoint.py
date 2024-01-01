def solve(A):
    cnt=0
    while len(set(A))!=1:
        new_A=[abs(int(A[i]) - int(A[i + 1])) for i in range(3)]+[abs(int(A[3])-int(A[0]))]
        A=new_A
        cnt+=1
    return cnt
while True:
    a=[i for i in input().split()]
    if all(int(x) == 0 for x in a):
        break
    print(solve(a))