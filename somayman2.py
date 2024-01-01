def check(n):
	for char in str(n):
		if char!='4' and char!='7':
			return False
	return True

n=int(input())
for _ in range(n):
	so=int(input())
	if check(so):
		print('YES')
	else:
		print('NO')