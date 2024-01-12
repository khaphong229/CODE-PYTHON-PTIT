n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# n,m=5,6
# a=[1, 2, 3, 4, 5]
# b=[3, 4, 5, 6, 7, 8]
A,B=set(a),set(b)
giao=sorted(A.intersection(B))
hieu=sorted(A.difference(B))
hieu2=sorted(B.difference(A))
print(*giao)
print(*hieu)
print(*hieu2)
