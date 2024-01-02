def tinhTong(so):
    tongChuSo=0
    for chuSo in str(so):
        tongChuSo+=int(chuSo)
    return tongChuSo
def kiemTraCachHaiDonVi(so):
    str_so=str(so)
    doDaiSo=len(str_so)
    kiemTra=set()
    for gtri in range(1,doDaiSo):
        khoangCach=abs(int(str_so[gtri])-int(str_so[gtri-1]))
        kiemTra.add(khoangCach)
    if 2 in kiemTra:
        return True
    else:
        return False

slgtest=int(input())
for _ in range(slgtest):
    so=int(input())
    if tinhTong(so)%10==0 and kiemTraCachHaiDonVi(so):
        print('YES')
    else:
        print('NO')
