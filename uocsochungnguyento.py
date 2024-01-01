from math import *
def prime(n):
	if n<2:
		return False
	for i in range(2,isqrt(n)+1):
		if n%i==0:
			return False
	return True

def ucln(a,b):
	while b!=0:
		a,b=b,a%b
	return a

def sum(n):
	tong=0
	while n!=0:
		tong+=n%10
		n//=10
	return tong

n=int(input())
for _ in range(n):
	a,b=map(int,input().split())
	if prime(sum(ucln(a,b))):
		print('YES')
	else:
		print('NO')