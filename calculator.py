
# CodeOrbit Tech - Python Programming Internship
# Project: Simple Calculator

def calculator():
    # Display the available operations
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            # Get the user's choice
            choice = input("\nChoose an operation (1-5): ")

            # Exit the calculator
            if choice == "5":
                print("Thank you for using the calculator!")
                break

            # Check whether the choice is valid
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice! Please select 1-5.")
                continue

            # Take two numbers as input
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the selected operation
            if choice == "1":
                result = num1 + num2
                operation = "+"
            elif choice == "2":
                result = num1 - num2
                operation = "-"
            elif choice == "3":
                result = num1 * num2
                operation = "*"
            else:
                # Prevent division by zero
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1 / num2
                operation = "/"

            # Display the result
            print(f"Result: {num1:g} {operation} {num2:g} = {result:g}")

        except ValueError:
            # Handle non-numeric input
            print("Invalid input! Please enter valid numbers.")


# Start the calculator program
if __name__ == "__main__":
    calculator()
