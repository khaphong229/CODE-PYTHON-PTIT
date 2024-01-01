def multi(n):
	temp=1
	for x in str(n):
		if x=='0':
			continue
		temp*=int(x)
	return temp

n=int(input())
for _ in range(n):
	num=int(input())
	print(multi(num))