so=int(input())
xau=str(so)
ds=[]
length=int(len(xau))
for i in range (-1,-length,-3):
	if length%3==0:
		ds.append(xau[i-2:i]+xau[i])
	else:
		ds.append(xau[i-2:i]+xau[i])
		if length+(i-2)==0:
			print(i)
			ds.append(xau[i:])
ds.reverse()
print(','.join(ds))