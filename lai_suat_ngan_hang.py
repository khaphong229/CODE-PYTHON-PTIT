def calculate_final_amount(N, X, M):
    years = 0
    while N < M:
        interest = N * (X / 100)
        N += interest
        years += 1
    return years

if __name__ == "__main__":
    n=int(input())
    for _ in range(n):
        n,x,m=map(float,input().split())
        print(calculate_final_amount(n,x,m))