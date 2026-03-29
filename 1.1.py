def typeTriangle(a, b, c):

    if a + b > c and a + c > b and b + c > a:
        if a == b == c :
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Normal"
    else:
        return "Not a triangle"
x = float(input("Enter three values : "))
y = float(input())
z = float(input())
print(typeTriangle(x, y, z))