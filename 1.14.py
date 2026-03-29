def UCLN(list_numbers):
    iteration = max(list_numbers)
    for i in range(iteration, 0, -1):
        if all(number % i == 0 for number in list_numbers):
            return i

def BCNN(list_numbers):
    i = max(list_numbers)
    multiply = 1
    while not all(i % number == 0 for number in list_numbers):
        i = max(list_numbers) * multiply 
        multiply += 1
    return i

def isPrime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def isSquare(num):
    root = num ** 0.5
    if root.is_integer():
        return True
    else:
        return False


def Square_Number(list_numbers):
    square_number = [num for num in list_numbers if isSquare(num)]
    return square_number

def Prime_Number(list_numbers):
    prime_number = [num for num in list_numbers if isPrime(num)]
    return prime_number

























def main():

    input_list = input("Nhập các số (cách nhau bởi dấu phẩy): ").split(",")
    input_list = list(map(int, input_list))

    print(f"UCLN của các số đã nhập là: {UCLN(input_list)}")
    print(f"BCNN của các số đã nhập là: {BCNN(input_list)}")
    print(f"Các số chính phương trong dãy đã nhập là: {Square_Number(input_list)}")
    print(f"Các số nguyên tố trong dãy đã nhập là: {Prime_Number(input_list)}")
    input_list.sort()
    print(f"Dãy số đã sắp xếp là: {input_list}")

if __name__ == "__main__":
    main()



