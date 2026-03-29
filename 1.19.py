import numpy as np


def SquareNumber(num):
    root = num ** 0.5
    if root.is_integer():
        return True
    else:
        return False
    
def SquareList(listNum):
    return len(list(filter(lambda x: SquareNumber(x), listNum)))

def PrimeList(listNum):
    return len(list(filter(lambda x: PrimeNumber(x), listNum)))

def PrimeNumber(num):
    if num <= 1:
        return False
    elif len(list(filter(lambda x : num % x == 0 , range(1,num+1)))) == 2:
        return True
    else:
        return False
    
def Sum(listNum):
    return sum(listNum)

def Average(listNum):
    return sum(listNum)/len(listNum)

def main():
    arrayNum = np.array(list(map(int , input("Input please :").split(' '))))
    print("Sum:", Sum(arrayNum))
    print("Average:", Average(arrayNum))
    print("Number of perfect squares:", SquareList(arrayNum))
    print("Number of prime numbers:", PrimeList(arrayNum))
    arrayNum.sort()

    print("Sorted list in descending order:", arrayNum[::-1])
if __name__ == "__main__":
    main()

