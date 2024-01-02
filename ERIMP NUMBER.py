import math
def prime(number):
	if number<2:
		return False
	for i in range(2,math.isqrt(number)+1):
		if number%i==0:
			return False
	return True

def reverse(number):
	rev=0
	while number!=0:
		rev=rev*10+(number%10)
		number//=10
	return rev

n=int(input())
for _ in range(n):
	list_numbers=[]
	number_input=int(input())
	for i in range(number_input+1):
		number_reversed=reverse(i)
		if i!=number_reversed and prime(i)==True and prime(number_reversed)==True and number_reversed<number_input:
			if i not in list_numbers and number_reversed not in list_numbers:
				list_numbers.append(i)
				list_numbers.append(number_reversed)
	for i in list_numbers:
		print(i,end=' ')
	print()
