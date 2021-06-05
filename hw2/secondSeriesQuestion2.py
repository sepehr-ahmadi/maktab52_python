import math

def primeNumber(num):
    if num > 1:
        for i in range(2, math.floor( math.sqrt(num)+ 1)):
            if (num % i) == 0:
                return False
        else:
             return True

    else:
        return False
def lowerPrimeNumbers(num):
    primeNumbersList=[]
    for i in range(2,num):
        if primeNumber(i)==True:
            primeNumbersList.append(i)
    return primeNumbersList
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
def primeDivisors(n):
    primeDivisorsList=[]

    while n % 2 == 0:
        primeDivisorsList.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            primeDivisorsList.append(i)
            n = n / i


    if n > 2:
        primeDivisorsList.append(n)

    return Remove(primeDivisorsList)
def listInput():
    numberOfInputs=int(input())
    ListValues=[]
    for i in range(0,numberOfInputs):
        ListValues.append(int(input()))
    return (ListValues)
def asgharoff(sangepaWeightList):
    sangpaPriceList=sangepaWeightList
    for i in range(0,len(sangepaWeightList)):
        if primeNumber(sangepaWeightList[i])==True:
            sangpaPriceList[i]=len(lowerPrimeNumbers(sangepaWeightList[i]))
        else:
            sangpaPriceList[i]=len(primeDivisors(sangepaWeightList[i]))
    return(sangpaPriceList)
def kianoshoff(sangepaPriceList):
    if(primeNumber(sum(sangepaPriceList)))==True:
        return sum(sangepaPriceList)-len(lowerPrimeNumbers(sum(sangepaPriceList)))
    else:
        return sum(sangepaPriceList)-len(primeDivisors(sum(sangepaPriceList)))
print(kianoshoff(asgharoff(listInput())))



