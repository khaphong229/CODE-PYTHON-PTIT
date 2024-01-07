soTest = int(input())
for _ in range(soTest):
	arr = [int(digit) for digit in input()]
	for i in range(len(arr) - 1, 0, -1):
		if arr[i] >= 5:
			arr[i - 1] += 1
		arr[i] = 0
	if arr[0] == 10:
		arr[0] = 0
		arr = [1] + arr
	for i in arr:
		print(i, end='')
	print()
