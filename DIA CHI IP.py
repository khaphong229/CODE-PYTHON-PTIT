def kiemTraIp(ip):
    thanhPhan=ip.split('.')
    if len(thanhPhan)!=4:
        return False
    for con in thanhPhan:
        if not con.isdigit() or not 0<=int(con)<=255:
            return False
    return True

if __name__=='__main__':
    slgTest=int(input())
    for _ in range(slgTest):
        ip=input()
        print('YES') if kiemTraIp(ip) else print('NO')