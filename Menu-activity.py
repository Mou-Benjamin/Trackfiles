def menu():
    attempts = 0
    while attempts < 3:
        print("\nMenu:")
        print("1. Add nunbers")
        print("2. Subtract numbers")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                print("The sum is: num1 + num2")
        elif choice == '2':
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                print("The difference is: num1 - num2")
        elif choice == '3':
                print("Exiting program...")
        else:
                print("Invalid option. Please try again.")
    attempts += 1 # Increment attempts counter by 1

# Call the menu function
menu()