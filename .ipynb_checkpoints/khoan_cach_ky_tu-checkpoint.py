def check(s):
    s_reversed=s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s_reversed[i]) - ord(s_reversed[i-1])):
            return False
    return True

if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        s=input()
        print('YES') if check(s) else print('NO')