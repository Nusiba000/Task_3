def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def factorial(n):
    if n < 0:
        return "Error: Negative number"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Factorial")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "0":
        print("Goodbye!")
        break

    elif choice == "6":
        n = int(input("Enter a number: "))
        print("Result:", factorial(n))

    elif choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", sum(a, b))
        elif choice == "2":
            print("Result:", difference(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        elif choice == "5":
            print("Result:", power(a, b))

    else:
        print("Invalid option. Please try again.")
