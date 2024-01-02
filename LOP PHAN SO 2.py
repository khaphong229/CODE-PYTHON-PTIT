from math import *
class PhanSo:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def toigian(self):
        ucln=gcd(self.tu,self.mau)
        self.tu//=ucln
        self.mau//=ucln
    def __add__(self,other):
        tong_tu=self.tu*other.mau+other.tu*self.mau
        tong_mau=self.mau*other.mau
        return PhanSo(tong_tu,tong_mau)
    def __str__(self):
        return f'{self.tu}/{self.mau}'
if __name__=='__main__':
    tu_p,mau_p,tu_q,mau_q=map(int,input().split())
    p=PhanSo(tu_p,mau_p)
    q=PhanSo(tu_q,mau_q)
    tong_p_q=p+q
    tong_p_q.toigian()
    print(tong_p_q)