def convert_to_primenumber(n):
    num = int(n)
    prime_list = []
    while num > 1:
        for i in range(2,num+1):
            if num % i == 0:
                prime_list.append(i)
                num = num // i
                break

    return prime_list

def IsPerfectNum(num):
    sum_num = 0
    store_num = []
    for i in range(1,num):
        if num % i == 0:
            store_num.append(i)
    for i in range(len(store_num)):
        sum_num += store_num[i]

    if sum_num == num:
        return True
    else:
        return False
    

def isPrimeNumber(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
num = int(input("Enter a positive integer: "))
print(f"{num} is perfect number" if IsPerfectNum(num) else f"{num} is not perfect number")
print(f"{num} is prime number" if isPrimeNumber(num) else f"{num} is not prime number")
print(f"The prime factorization of {num} is: {convert_to_primenumber(num)}")
print(f"{num} is palindrome" if isPalindrome(str(num)) else f"{num} is not palindrome")