def solve(string):
	length=len(string)
	for char in range(0,length,2):
		print(string[char]*int(string[char+1]),end='')
	print()

n=int(input())
for _ in range(n):
	num_input=input()
	solve(num_input)