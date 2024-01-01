class SinhVien:
    def __init__(self,ten,sinh,mon1,mon2,mon3,tong):
        self.ten=ten
        self.sinh=sinh
        self.mon1=mon1
        self.mon2=mon2
        self.mon3=mon3
        self.tong=tong
    def chuanHoa(self):
        if self.sinh[1]=='/':
            self.sinh='0'+self.sinh
        if self.sinh[4]=='/':
            self.sinh=self.sinh[0:3]+'0'+self.sinh[3:]
    def total(self):
        self.tong=self.mon1+self.mon2+self.mon3
    def __str__(self):
        return f'{self.ten} {self.sinh} {self.tong}'
ten=input()
sinh=input()
mon1=float(input())
mon2=float(input())
mon3=float(input())
tong=0
sv=SinhVien(ten,sinh,mon1,mon2,mon3,tong)
sv.chuanHoa()
sv.total()
print(sv)