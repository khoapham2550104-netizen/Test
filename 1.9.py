def FrequencyofChars(string):
    available_chars = []

    for char in string:
        if char in available_chars:
            pass
        else:
            available_chars.append(char)
    for i in range(len(available_chars)):
        print(f"{available_chars[i]}: {string.count(available_chars[i])}")

string = input("Enter a string: ")
FrequencyofChars(string)