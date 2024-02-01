class SinhVien:
    def __init__(self,ma,mon,hthuc):
        self.ma=ma
        self.mon=mon
        self.hthuc=hthuc
    def ma_mon(self):
        return self.ma
    def __str__(self):
        return f'{self.ma} {self.mon} {self.hthuc}'

n=int(input())
a=[]
for i in range(n):
    s=SinhVien(input(),input(),input())
    a.append(s)
a.sort(key=lambda x : x.ma_mon())
for x in a:
    print(x)
