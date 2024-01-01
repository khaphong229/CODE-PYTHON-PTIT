def check_base_3(s):
    for char in s:
        if char not in ['0', '1', '2']:
            return False
    return True

t=int(input())
for _ in range(t):
    s=input()
    print('YES') if check_base_3(s) else print('NO')