n=int(input())
start='2'+'0'*(n-1)
end='9'*n
for i in range(int(start),int(end)+1):
	if '2' in str(i) and '3' in str(i) and '5' in str(i) and '7' in str(i):
		if '1' not in str(i) and '4' not in str(i) and '6' not in str(i) and '8' not in str(i) and '9' not in str(i) and '0' not in str(i):
			if i%2==1:
				print(i)