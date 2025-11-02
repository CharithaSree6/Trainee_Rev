# Extract digits from Tuple list.

data = [(12, 34), (56, 78), (90, 1)]

digits = []

for tup in data:
    for num in tup:
        digits.extend(map(int, str(num)))

print(digits)