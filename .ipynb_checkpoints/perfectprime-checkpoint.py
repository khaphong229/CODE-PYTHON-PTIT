from math import *
def prime(n):
	n=int(n)
	if n<2:
		return False
	for i in range(2,isqrt(n)+1):
		if n%i==0:
			return False
	return True
def reverse(n):
	numReversed=str(n)[::-1]
	return numReversed
def sum(n):
	total=0
	while n!=0:
		total+=n%10
		n//=10
	return total

def check_prime(n):
	for x in str(n):
		if prime(int(x))==False:
			return False
	return True
	
n=int(input())
for _ in range(n):
	numInput=int(input())
	if prime(numInput) and prime(reverse(numInput)) and prime(sum(numInput)) and check_prime(numInput):
		print('Yes')
	else:
		print('No')