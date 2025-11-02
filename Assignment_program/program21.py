#Python program to find N largest elements from a list.
numbers = [10, 50, 4, 20, 15, 100, 75]
N = 3

# Sort list in descending order
numbers.sort(reverse=True)

print(f"{N} largest elements are:", numbers[:N])