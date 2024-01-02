def check(n):
	str_n=str(n)
	for i in range(len(str_n)):
		if str_n[i:i+2]==str[i+1:i+3]:
			return True
		else:
			return False
n=int(input())
for _ in range(n):
	num=int(input())
	if check(num):
		print('YES')
	else:
		print('NO')