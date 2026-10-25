import numpy as np

# User enters the size of the array
n = int(input("Enter the number of elements: "))

# User enters array elements
elements = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    elements.append(value)

# Create NumPy array
arr = np.array(elements)

print("\nOriginal Array:")
print(arr)

# Indexing
index = int(input("\nEnter index position to view element: "))
if 0 <= index < len(arr):
    print("Element at index", index, "=", arr[index])
else:
    print("Invalid index!")

# Slicing
start = int(input("\nEnter starting index for slicing: "))
end = int(input("Enter ending index for slicing: "))
print("Sliced Array:", arr[start:end])

# Mathematical Operations
print("\nMathematical Operations:")
print("Sum =", np.sum(arr))
print("Mean =", np.mean(arr))
print("Maximum =", np.max(arr))
print("Minimum =", np.min(arr))

# Edit Value
choice = input("\nDo you want to edit any value? (yes/no): ")

if choice.lower() == "yes":
    pos = int(input("Enter index to modify: "))
    new_value = int(input("Enter new value: "))

    if 0 <= pos < len(arr):
        arr[pos] = new_value
        print("\nUpdated Array:")
        print(arr)
    else:
        print("Invalid index!")

print("\nFinal Array:")
print(arr)