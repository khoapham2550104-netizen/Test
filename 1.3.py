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
    
num = int(input("Enter a positive integer: "))
print(f"{num} is perfect number" if IsPerfectNum(num) else f"{num} is not perfect number")