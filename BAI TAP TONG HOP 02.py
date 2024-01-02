import re
#test case: xin chao....cac ban. toi la   phong??
#a
s=input()
#b
print('YES') if len(s)%2==0 else print('NO')
#c
s=check(s)
a=s.split('.')
print(len(a))
#d
def xoa_space(s):
    a=s.split()
    b=' '.join(a)
    return b
def check(s):
    s=re.sub(r'\.{2,}', '.', s)
    s=re.sub(r'\?{2,}', '?', s)
    return s
    
ds_cau_moi=[]

for i in a:
    str_i=str(i)
    result=xoa_space(check(str_i)).capitalize()
    ds_cau_moi.append(result)
    print(result)
#e
print(sorted(ds_cau_moi))
#f
for i in ds_cau_moi:
    print(i,end=' ')