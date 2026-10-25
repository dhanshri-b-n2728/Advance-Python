import csv
import json

# User enters file names
csv_file = input("Enter CSV file name (e.g., data.csv): ")
json_file = input("Enter JSON output file name (e.g., output.json): ")

try:
    # Read CSV data
    data = []

    with open(csv_file, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            data.append(row)

    # Write JSON data
    with open(json_file, mode='w') as file:
        json.dump(data, file, indent=4)

    print(f"\nCSV data successfully converted to '{json_file}'")

except FileNotFoundError:
    print("CSV file not found. Please check the file name.")