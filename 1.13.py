binnary_input = input("Enter a binary number: ").split(",")
#Check if the input is divisible by 5

for bin in binnary_input:
    decimal_output = int(bin, 2) #Convert binary to decimal (number 2 implies base 2)
    if decimal_output % 5 == 0:
        print(f"{bin} is divisible by 5")
    else:
        print(f"{bin} is not divisible by 5")


