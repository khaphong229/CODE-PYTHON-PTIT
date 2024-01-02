def adverse_pair(length, listA):
    count = 0
    for index in range(length - 1):
        for index1 in range(index + 1, length):
            if listA[index] > listA[index1]:
                count += 1
    return count


length = int(input())
listInput = list(map(int, input().split()))
print(adverse_pair(length, listInput))
