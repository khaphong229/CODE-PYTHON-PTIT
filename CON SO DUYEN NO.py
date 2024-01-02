n=int(input())
for _ in range(n):
	num_input=input()
	if num_input[0]==num_input[-1]:
		print('YES')
	else:
		print('NO')