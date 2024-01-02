def minNumber(string):
	superMax=float('-inf')
	temp=0
	for char in string:
		if char.isdigit():
			temp=temp*10+int(char)
		else:
			if temp!=0:
				superMax=max(superMax,temp)
				temp=0
	if temp!=0:
		superMax=max(superMax,temp)
        
	return superMax

n=int(input())
for _ in range(n):
	stringInput=input()
	print(minNumber(stringInput))