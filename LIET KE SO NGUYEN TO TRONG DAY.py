from math import *
def prime(n):
	if n<2:
		return False
	for i in range(2,isqrt(n)+1):
		if n%i==0:
			return False
	return True
if __name__=='__main__':
    n=int(input())
    ds=[int(i) for i in input().split()]
    list_prime=dict({})
    for i in ds:
        if prime(i):
            if i in list_prime:
                list_prime[i]+=1
            else:
                list_prime[i]=1
    for i in list_prime:
        print(f'{i} {list_prime[i]}')