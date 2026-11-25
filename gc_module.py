import gc

# Check GC status
print("Garbage Collection Enabled:", gc.isenabled())

# Display object count before creating objects
print("\nGC Counts Before Object Creation:")
print(gc.get_count())

# Create large objects
data = []

for i in range(10000):
    data.append([j for j in range(100)])

print("\nGC Counts After Object Creation:")
print(gc.get_count())

# Delete object references
del data

print("\nAfter Deleting References:")
print(gc.get_count())

# Perform Manual Garbage Collection
collected = gc.collect()

print("\nManual Garbage Collection Performed")

print("Objects Collected:", collected)

print("\nGC Counts After Collection:")
print(gc.get_count())