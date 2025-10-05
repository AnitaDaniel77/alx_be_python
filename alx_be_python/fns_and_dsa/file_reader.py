def read_file():
    print("Read a File")

    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("That file does not exist.")
    except Exception:
        print("Something went wrong while reading the file.")

if __name__ == "__main__":
    read_file()
