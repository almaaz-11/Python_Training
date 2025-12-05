

def main() -> None:
    print("Welcome to the Calculator")
    print("-" * 40)

    while True:
        try:
            num1 = float(input('Enter first number: '))
            print("Select Operation: +, -, *, /, **")
            operation = input("Enter operation: ")
            num2 = float(input('Enter second number: '))
            
            if operation == '+':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero")
                    continue
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            elif operation == '**':
                if num2 < 0:
                    print("Error: Exponent cannot be negative")
                    continue
                result = num1 ** num2
                print(f"{num1} ** {num2} = {result}")
            else:
                print("Invalid operation")

            continue_choice = input("Perform another calculation? (yes/no): ").lower()
            if continue_choice not in ['yes', 'y']:
                print("Thank you for using the calculator")
                break
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()