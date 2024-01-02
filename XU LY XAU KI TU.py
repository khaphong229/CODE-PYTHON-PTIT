def xu_ly(s):
    s=s.lower()
    tap_tu=set(s.split())
    return sorted(tap_tu)

def hop_giao(tap1,tap2):
    hop=sorted(set(tap1).union(tap2))
    giao=sorted(set(tap1).intersection(tap2))
    return hop, giao

s1=input()
s2=input()
tap1=xu_ly(s1)
tap2=xu_ly(s2)
hop,giao=hop_giao(tap1,tap2)
print(' '.join(hop))
print(' '.join(giao))