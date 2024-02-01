d = {}
a = []
cnt_ap = {}

n = int(input())
for _ in range(n) :
    id = input()
    name = input()
    clas = input()
    d = {
        'cntid' : 0 ,
        'id' : id ,
        'name' : name ,
        'clas' : clas
    }
    cnt_ap[id] = 10
    a.append(d)
for _ in range(n) :
    id , diemdanh  = [str(i) for i in input().split()]
    for i in diemdanh :
        if (i == 'm') :
            cnt_ap[id] -= 1
        if (i == 'v') :
            cnt_ap[id] -= 2

        if (cnt_ap[id] <= 0) :
            cnt_ap[id] = "0 KDDK"
            break

for i in range(n) :
    print(a[i]["id"] , a[i]["name"] ,a[i]["clas"] , cnt_ap[a[i]["id"] ])