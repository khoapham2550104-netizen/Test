class Calculate:
    def calA(n):
        sum_A = 0
        for i in range(0, n+1):
            sum_A += i**2
        return sum_A    
    def calB(n):
        sum_B = 0
        for i in range(0, n):
            sum_B += (2*i + 1)**2
        return sum_B
    def calC(n):
        sum_C = 0
        for i in range(1, n+1):
            sum_C += (-1)**(i-1) / (2*i)**2
        return sum_C
    


    def calD(n):
        sum_D = 0
        multiply = 1
        for i in range(1, n+1):
            for j in range(1,i+1):
                multiply *= j
            sum_D += multiply
            multiply = 1
        return sum_D
    

n = int(input("Enter a positive integer n: "))
print(f"calA: {Calculate.calA(n)}")
print(f"calB: {Calculate.calB(n)}")
print(f"calC: {Calculate.calC(n)}")
print(f"calD: {Calculate.calD(n)}")