# Create a Python list and demonstrate list slicing and appending new elements.

numbers = [10, 20, 30, 40, 50, 60]

# List slicing
print("Original list:", numbers)
print("Slice from index 1 to 4:", numbers[1:4])   # elements at index 1,2,3
print("Slice from start to index 3:", numbers[:3]) # first three elements
print("Slice from index 2 to end:", numbers[2:])   # elements from index 2 to the end
print("Full slice (copy of list):", numbers[:])    # whole list

# Appending
numbers.append(70)
numbers.append(80)

print("List after appending:", numbers)