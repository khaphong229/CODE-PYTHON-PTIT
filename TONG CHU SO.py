def sumOfDigits(number):
    return sum(ord(digit)-ord('0') for digit in str(number))

def countStep(number):
    steps=0
    if number<10:
        return 1
    while number>=10:
        number=sumOfDigits(number)
        steps+=1
    return steps
inputNumber=int(input())
print(countStep(inputNumber))