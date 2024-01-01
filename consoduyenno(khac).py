def check(n):
	cuoi=n%10
	while n>=10:
		n//=10
	if n==cuoi:
		return True
	return False
n=int(input())
for _ in range(n):
	num_input=int(input())
	if check(num_input):
		print('YES')
	else:
		print('NO')