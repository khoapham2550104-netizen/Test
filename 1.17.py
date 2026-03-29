def SortLength(strings):
    sorted_string = sorted(strings, key=len)
    return sorted_string

def main():
    strings = input("Enter strings separated by commas: ").split(' ')
    for i, value in enumerate(SortLength(strings)):
        print(f"{len(value)} : {value}")

if __name__ == "__main__":
    main()
