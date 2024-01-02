def check(N):
    sum_of_digits = sum(int(digit) for digit in str(N))
    property_1 = sum_of_digits % 10 == 0

    str_N = str(N)
    property_2 = all(abs(int(str_N[i]) - int(str_N[i + 1])) == 2 for i in range(len(str_N) - 1))

    return property_1 and property_2

n=int(input())
for _ in range(n):
	N=int(input())
	if check(N):
		print('YES')
	else:
		print('NO')