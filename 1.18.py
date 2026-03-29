def CheckVar(listA, listB):
    setA = set(listA)
    setB = set(listB)
    lengthA = len(setA)
    set_intersection = setA.intersection(setB)
    length_intersection = len(set_intersection)
    return length_intersection/lengthA
    
def main():
    listA = input("Enter first list of items separated by commas: ").split(' ')
    listB = input("Enter second list of items separated by commas: ").split(' ')
    if CheckVar(listA, listB) >= 0.6:
        print("The lists are similar.")
    elif CheckVar(listA, listB) <= 0.2:
        print("The lists are not similar.")
    else:
        print("The lists are somewhat similar.")

if __name__ == "__main__":
    main()
