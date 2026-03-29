n = int(input("Enter a positive integer: "))
d = {}
for i in range(1,n+1):

    d.update({i: i*i})
print(d)