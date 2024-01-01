def check(n):
    length = len(n)
    for i in range(length - 1):
        if n[i + 1] < n[i]:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        num = input()
        if check(num):
            print('YES')
        else:
            print('NO')
