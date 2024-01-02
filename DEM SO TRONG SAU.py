def count_numbers_in_string(s,n):
    length_s=len(s)
    length_n=len(n)
    cnt=0
    i=0
    while i<=length_s-length_n+1:
        if s[i:length_n+i]==n:
            cnt+=1
            i+=length_n
        else:
            i+=1
    return cnt

t=int(input())
for _ in range(t):
    s=input()
    n=input()
    print(count_numbers_in_string(s,n))