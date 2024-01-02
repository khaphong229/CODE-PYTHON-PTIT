def commonElements(a, b, c):
    A = set(a)
    B = set(b)
    C = set(c)
    AgiaoB = A.intersection(B)
    AgiaoBgiaoC = AgiaoB.intersection(C)
    if len(AgiaoBgiaoC)>0:
        return AgiaoBgiaoC
    else:
        return False


amountTest = int(input())
for test in range(amountTest):
    amountA, amountB, amountC = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    result=commonElements(a,b,c)
    if result:
        for index in result:
            if index in a:
                print(index,end=' ')
    else:
        print('NO')
