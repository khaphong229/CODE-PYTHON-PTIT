def solve(n):
    while len(n)%3!=0:
        n='0'+n
    s=''
    for i in range(0,len(n),3):
        ba=n[i:i+3]
        thap_phan=int(ba,2)
        s+=str(thap_phan)
    return s
        
if __name__=='__main__':
    n=input()
    print(solve(n))