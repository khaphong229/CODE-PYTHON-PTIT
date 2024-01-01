import random
#a
random_numbers = [random.randint(0, 50) for _ in range(100)]
print(random_numbers)
#b
print(", ".join(map(str, random_numbers)))
#c
trungbinh = sum(random_numbers) / len(random_numbers)
print(trungbinh)
#d
loc = [num for num in random_numbers if '2' in str(num) or '8' in str(num)]
print(", ".join(map(str, loc)))