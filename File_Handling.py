# User enters file names
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

try:
    # Read data from input file
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Count total lines
    line_count = len(lines)

    print("\nTotal Number of Lines:", line_count)

    # Extract first two lines
    extracted_lines = lines[:2]

    print("\nFirst Two Lines:")
    for line in extracted_lines:
        print(line.strip())

    # Write extracted lines to output file
    with open(output_file, "w") as file:
        file.writelines(extracted_lines)

    print(f"\nExtracted data successfully written to '{output_file}'")

except FileNotFoundError:
    print("Input file not found. Please check the file name.")