def solve(s):
    text=[]
    digit=[]
    for i in s:
        if i.isalpha():
            text.append(i)
        else:
            digit.append(int(i))
    
    return sorted(text), sum(digit)
n=int(input())
for _ in range(n):
    s=input()
    result=solve(s)
    for i in result[0]:
        print(i,end='')
    print(result[1])