def update_account(storage):
    account = input("Enter your account name: ")
    password = input("Enter your password: ")
    storage.update({account: password})
    print("Updating a new account...")

def sign_in(storage):
    account = input("Enter your account name: ")
    password = input("Enter your password: ")
    try:
        if account in storage and storage.get(account) == password:
            print("Sign in successful!")
            print("Signing in to existing account... ")
        else:  
            print("Sign in failed! Incorrect account name or password.")
    except KeyError:
        print("Sign in failed! Incorrect account name or password.")

def find_account(storage):
    account = input("Enter your account name to find: ")
    try:
        if account in storage:
            print(f"Account '{account}' found.")
        else:
            print(f"Account '{account}' not found.")
    except:
        print(f"Account '{account}' not found.")



def main():
    storage = {}
    condition = True
    while condition:
        choices = input("Enter your choice \n1. Update a new account \n2. Sign in to existing account \n3. Find your account \n4. Exit \n")
        match choices:
            case "1":
                update_account(storage)
            case "2":
                sign_in(storage)
            case "3":
                find_account(storage)
            case "4":
                condition = False
            case _:
                print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()