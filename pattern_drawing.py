size_input = input("Enter the size of the pattern: ")

try:
    size = int(size_input)

    if size <= 0:
        print("Please enter a positive number.")
    else:
        row = 0
        while row < size:
            for column in range(size):
                print("*", end="")
            print()
            row += 1

except ValueError:
    print("Oops! That wasn't a valid number. Please enter a positive integer.")
