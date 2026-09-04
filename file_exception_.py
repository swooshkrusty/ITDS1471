# Python file for exception handling
# write text to a file
def main():
    """Main function as entry point."""
    filename = input("Enter the filename: ")
    write_to_file(filename)
    read_file(filename)

def write_to_file(filename):
    """Write text to a file."""
    try:
        with open(filename, "w") as outfile:
            for i in range(1, 11):
                outfile.write(f" {i} {i * 2} {i ** 2}\n")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except PermissionError:
        print(f"You can access this file: {filename}")
    except Exception as ex:
        print(ex)
    else:
        print("No errors occurred")
    finally: 
        print("error or not, you will come to this block")

def read_file(filename):
    """Read text from a file."""
    try:
        with open(filename, "r", encoding="utf-8") as infile:
            for line in infile:
                nums_string = line.split()
                nums = [int(num) for num in nums_string]
                print(nums) 
            
            # data = infile.read()
            # print(data)
            
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except PermissionError:
        print(f"You do not have permission to open: {filename}")
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()