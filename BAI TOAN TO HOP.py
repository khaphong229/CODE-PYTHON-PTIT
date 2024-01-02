from itertools import combinations

def lexico_combinations(arr, k):
    result = []
    unique_elements = list(set(arr))
    unique_combinations = combinations(sorted(unique_elements), k)
    for comb in unique_combinations:
        result.append(" ".join(map(str, comb)))
    return result

N, K = map(int, input().split())
A = list(map(int, input().split()))
result = lexico_combinations(A, K)
for r in result:
    print(r)