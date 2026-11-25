import threading
import time


# Task 1: Counting numbers
def count_numbers(limit):
    for i in range(1, limit + 1):
        print(f"[Count Thread] Count: {i}")
        time.sleep(0.5)  # Pause briefly to make concurrent execution visible


# Task 2: Calculating squares
def calculate_squares(numbers):
    for num in numbers:
        print(f"[Square Thread] Square of {num}: {num ** 2}")
        time.sleep(0.5)


# Task 3: Calculating cubes
def calculate_cubes(numbers):
    for num in numbers:
        print(f"[Cube Thread] Cube of {num}: {num ** 3}")
        time.sleep(0.5)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    # Create three separate thread objects
    t1 = threading.Thread(target=count_numbers, args=(5,))
    t2 = threading.Thread(target=calculate_squares, args=(nums,))
    t3 = threading.Thread(target=calculate_cubes, args=(nums,))

    # Start all threads concurrently
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to finish before exiting the main program
    t1.join()
    t2.join()
    t3.join()

    print("All tasks completed!")