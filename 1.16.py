#Employee management system
"""class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"""


def salary_sum(members_salary):
    salary = []
    sum_salary = 0
    for value in members_salary.values():
        salary.append(value)
    sum_salary = sum(salary)    
    return sum_salary

def add_employee(members_salary):
    name = input("Enter employee's name:")
    salary = int(input("Enter employee's salary:"))
    members_salary.update({name: salary})
    return members_salary

def remove_employee(members_salary):
    name = input("Enter employee's name to remove:")
    if name in members_salary:
        members_salary.pop(name)
    else:
        print("Employee not found.")
    return members_salary

def display_employees(members_salary):
    for name, salary in members_salary.items():
        print(f"Name: {name}, Salary: ${salary}")

def main():
    members_salary = {}
    members_salary_new = dict(sorted(members_salary.items()))
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display Employees")
        print("4. Calculate Total Salary")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            members_salary = add_employee(members_salary_new)
        elif choice == '2':
            members_salary = remove_employee(members_salary_new)
        elif choice == '3':
            display_employees(members_salary_new)
        elif choice == '4':
            total_salary = salary_sum(members_salary_new)
            print(f"Total Salary of all employees: ${total_salary}")
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    