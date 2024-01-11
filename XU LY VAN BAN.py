import re


res=''
regex='\\.\\!\\?'

while True:
    try: res+=input()
    except EOFError: break
res=re.split(regex,res)

for i in res:
    x=i.lower().split()
    x[0]=x[0].title()
    print(*x)