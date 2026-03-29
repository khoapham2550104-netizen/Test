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

n = int(input("Enter a positive integer n: "))
for i in range(len(convert_to_primenumber(n))):
    print(convert_to_primenumber(n)[i], end=" ")
    if i < len(convert_to_primenumber(n)) - 1:
        print(".", end=" ") 
    else :
        pass