def check(n):
	if n[-2:]=='86':
		print('YES')
	else:
		print('NO')
n=int(input())
for _ in range(n):
	numInput=input()
	check(numInput)