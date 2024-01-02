n=int(input())
list_loi_chuc=[]
for _ in range(n):
    loi_chuc=input()
    list_loi_chuc.append(loi_chuc)
print(len(set(list_loi_chuc)))