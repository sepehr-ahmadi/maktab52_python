def divisors(n):
    divisorsList = []
    i = 1
    while i <= n:
        if n % i == 0:
            divisorsList.append(i)
        i = i + 1
    return len(divisorsList)


numbersOfDivisors = int(input())
i = 1
goodNumber = 1
while True:
    if divisors(goodNumber) == numbersOfDivisors:
        print(goodNumber)
        break
    else:
        i += 1
        goodNumber += i
