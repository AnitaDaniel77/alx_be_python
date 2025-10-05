def divide_numbers():
    print("Divide Two Numbers")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    divide_numbers()
