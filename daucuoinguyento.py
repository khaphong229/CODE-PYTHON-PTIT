from math import *
def prime(n):
	if n<2:
		return False
	for i in range(2,isqrt(n)+1):
		if n%i==0:
			return False
	return True

n=int(input())
for _ in range(n):
	num=input()
	if prime(int(num[:3])) and prime(int(num[-3:])):
		print('YES')
	else:
		print('NO')