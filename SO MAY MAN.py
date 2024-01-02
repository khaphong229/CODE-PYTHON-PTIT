n=int(input())
ds=[0]*10
for i in str(n):
	ds[int(i)]+=1
if ds[7]+ds[4]==4 or ds[7]+ds[4]==7:
	print('YES')
else:
	print('NO')