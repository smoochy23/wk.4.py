def modify_file(input_filename, output_filename):
    """
    Reads a file, modifies its content (uppercases each line),
    and writes the modified content to a new file.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write to.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                modified_line = line.upper()
                outfile.write(modified_line)
        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read from or write to the file(s). Please check permissions.")

if __name__ == "__main__":
    while True:
        input_file = input("Enter the name of the file you want to read: ")
        try:
            with open(input_file, 'r') as f:
                # Attempt to read a line to check if the file exists and is readable
                f.readline()
            break  # Exit the loop if the file can be opened for reading
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' does not exist. Please try again.")
        except IOError:
            print(f"Error: Could not read the file '{input_file}'. Please check permissions and try again.")

    output_file = input("Enter the name for the new output file: ")
    modify_file(input_file, output_file)

    print("\n🎉 File Read & Write Challenge and Error Handling Lab completed!")
    print("You are now skilled in managing files and handling potential errors in Python.")