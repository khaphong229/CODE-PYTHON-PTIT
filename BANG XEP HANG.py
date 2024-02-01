listSv=[]
# listSv = [{'ten': 'Nguyen Van Nam', 'dung': 168, 'tong': 600},
#           {'ten': 'Tran Thi Ngoc', 'dung': 168, 'tong': 600}]
for _ in range(int(input())):
    name=input()
    a=name.split()
    tenb=' '.join(a).title()
    correct,total=map(int,input().split())
    sv={
        'ten':tenb,
        'dung':correct,
        'tong':total,
    }
    listSv.append(sv)
listSv.sort(key= lambda x : (-x['dung'],x['tong'],x['ten']))
for i in range(len(listSv)):
    for j in listSv[i].values():
        print(j,end=' ')
    print()