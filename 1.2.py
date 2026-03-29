import math
from math import e

def function1(x):
    if x > 0:
        return 3*x + math.sqrt(x)
    else:
        return math.e**x + 4
def function2(x):
    if x >= 1 :
        return math.sqrt(x**2 + 1)
    elif -1 < x < 1:
        return 3*x + 5
    else:
        return x**2 + 2*x - 1
    
x = float(input("Enter a value x: "))
print("function1:", function1(x))
print(f"function2: {function2(x)} ")