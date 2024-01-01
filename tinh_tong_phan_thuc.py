n=int(input())
for _ in range(n):
    num=int(input())
    if num%2==0:
        sum=0
        for i in range(2,num+1,2):
            sum+=1/i
        print('{:.6f}'.format(sum))
    else:
        sum=0
        for i in range(1,num+1,2):
            sum+=1/i
        print('%.6f'%sum)