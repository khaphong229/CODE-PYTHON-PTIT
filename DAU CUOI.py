def check(num):
	if num[:2]==num[-2:]:
		return True
	return False

n=int(input())
for _ in range(n):
	num_input=input()
	print('YES') if check(num_input) else print('NO')