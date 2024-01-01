xau=str(input())
hoa, thuong=0, 0
for char in xau:
	if char.isupper():
		hoa+=1
	if char.islower():
		thuong+=1
if hoa>thuong:
	print(xau.upper())
else:
	print(xau.lower())