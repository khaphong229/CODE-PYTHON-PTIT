import math
def prime(n):
	if n<2:
		return False
	for i in range(2,math.isqrt(n)+1):
		if n%i==0:
			return False
	return True

def sum(n):
	sum=0
	while n!=0:
		sum+=n%10
		n//=10
	return sum

n=int(input())
for _ in range(n):
	num_input=int(input())
	if prime(sum(num_input)):
		print('YES')
	else:
		print('NO')