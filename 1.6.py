def list(list1, list2):
    if len(list1) > len(list2):
        return list1
    elif len(list1) < len(list2):
        return list2
    else:
        return list1, list2
    
list1 = input("Enter 1")
list2 = input("Enter 2")

print(list(list1,list2))
