def chen_xau(S1, S2, p):
    return S1[:p-1] + S2 + S1[p-1:]

s1=input()
s2=input()
p=int(input())
print(chen_xau(s1, s2, p))