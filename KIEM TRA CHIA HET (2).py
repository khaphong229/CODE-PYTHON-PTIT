def count_numbers(L, R, N):
    count = 0
    for num in range(L, R + 1):
        divisible = False
        for divisor in range(2, N + 1):
            if num % divisor == 0:
                divisible = True
                break
        if not divisible:
            count += 1
    return count

l,r=map(int,input().split())
n=int(input())
print(count_numbers(l,r,n))