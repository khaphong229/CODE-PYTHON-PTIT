file1 = open('CONTACT.in', 'r')
line = file1.readlines()
d=dict({})
ans=[]
for i in line:
    a=i.strip().split('@')
    a[0]=a[0].lower()
    a[1]=a[1].lower()
    b=a[0]+'@'+a[1]
    if b not in ans:
        ans.append(b)
ans.sort()
for i in ans:
    print(i)