import time

def egg_timer():
    print("How do you like you egg?")
    print("1. Soft-Bioled")
    print("2. Medium-Boiled")
    print("3. Hard-Boiled")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        cook_time = 5
    elif choice == '2':
        cook_time = 8
    elif choice == '3':
        cook_time = 12
    else:
        print("Invalid choice! Please select a valid option.")
        return 
        