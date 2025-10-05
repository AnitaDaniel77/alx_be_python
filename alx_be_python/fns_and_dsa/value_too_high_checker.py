# Custom error
class ValueTooHighError(Exception):
    pass

def check_number():
    print("Check if Number is Too High")

    try:
        number = int(input("Enter a number: "))
        if number > 100:
            raise ValueTooHighError("Number is too high. Must be 100 or less.")
        print("You entered:", number)
    except ValueTooHighError as error:
        print(error)
    except ValueError:
        print("Please enter a whole number.")

if __name__ == "__main__":
    check_number()
