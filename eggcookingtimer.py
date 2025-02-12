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
        
    print(f"Starting timer for {cook_time} minutes...")
    for remaining_time in range(cook_time *60, 0, -1):
        minutes, seconds = divmod(remaining_time, 60)
        time.sleep(1)
        print(f"Time remaining: {minutes: 02}:{seconds:02}", end="\r")
    print("\Your egg is ready! Enjoy!")

egg_timer()