class GiaoVien:
    def __init__(self,ma,ten,maGv,tin,chMon):
        self.ma='GV'+format(ma,'02d')
        self.ten=ten
        self.maGv=maGv
        self.tin=tin
        self.chMon=chMon

    def get_mon(self):
        if self.maGv[0]=='A': sj='TOAN'
        elif self.maGv[0]=='B': sj='LY'
        else: sj='HOA'
        return sj

    def tong(self):
        tong=self.tin*2+self.chMon
        if self.maGv[1]=='1': tong+=float(2)
        elif self.maGv[1]=='2': tong+=float(1.5)
        elif self.maGv[1]=='3': tong+=float(1)
        else: tong+=float(0)
        return tong

    def status(self):
        c=self.tong()
        if c>18.0: return 'TRUNG TUYEN'
        else: return 'LOAI'
    def __str__(self):
        return f'{self.ma} {self.ten} {self.get_mon()} {self.tong()} {self.status()}'


if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(n):
        ten=input()
        maGv=input()
        tin=float(input())
        chMon=float(input())
        s=GiaoVien(i+1,ten,maGv,tin,chMon)
        a.append(s)
    a.sort(key=lambda x: -x.tong())
    for x in a:
        print(x)





