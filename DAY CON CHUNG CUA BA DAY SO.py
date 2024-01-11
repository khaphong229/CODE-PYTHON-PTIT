def find(n, m, k, h1, h2, h3):
    check, cnt1, cnt2, cnt3 = 0, 0, 0, 0
    while cnt1<n and cnt2<m and cnt3<k:
        if h1[cnt1]==h2[cnt2]==h3[cnt3]:
            print(h1[cnt1],end=' ')
            check=1
            cnt1,cnt2,cnt3=cnt1+1,cnt2+1,cnt3+1
        elif h1[cnt1]<=h2[cnt2] and h1[cnt1]<=h3[cnt3]:
            cnt1+=1
        elif h2[cnt2]<=h3[cnt3] and h2[cnt2]<=h1[cnt1]:
            cnt2+=1
        else:
            cnt3+=1
    if check==0:
        print('NO')
    print()


if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n,m,k=map(int,input().split())
        h1=[int(i) for i in input().split()]
        h2=[int(i) for i in input().split()]
        h3=[int(i) for i in input().split()]
        find(n,m,k,h1, h2, h3)