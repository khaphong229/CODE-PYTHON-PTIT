a = str(input())
def nb(x_k):
    th_g = sum(1 for char in x_k if char.islower())
    h_oa = sum(1 for char in x_k if char.isupper())
    if th_g > h_oa:
        return x_k.lower()
    else:
        return x_k.upper()
kq = nb(a)
print(kq)