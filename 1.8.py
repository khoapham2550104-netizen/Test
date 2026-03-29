def CountUpperCaseLetters(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count

def CountLowerCaseLetters(s):
    count = 0
    for char in s:
        if char.islower():
            count += 1
    return count

s = input("Enter a string: ")
print(f"Number of uppercase letters: {CountUpperCaseLetters(s)}")
print(f"Number of lowercase letters: {CountLowerCaseLetters(s)}")