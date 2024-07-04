# Simple Calculator Program with Loop

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Welcome to Simple Calculator!")
    
    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter operation number (1/2/3/4/5): "))
            if choice == 5:
                print("Exiting calculator. Goodbye!")
                break
            elif choice in (1, 2, 3, 4):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == 1:
                    result = add(num1, num2)
                    operation = '+'
                elif choice == 2:
                    result = subtract(num1, num2)
                    operation = '-'
                elif choice == 3:
                    result = multiply(num1, num2)
                    operation = '*'
                elif choice == 4:
                    result = divide(num1, num2)
                    operation = '/'

                print(f"\n{num1} {operation} {num2} = {result}")
            else:
                print("Invalid input! Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    calculator()
