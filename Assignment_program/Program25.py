# Print anagrams together in Python using List and Dictionary.

words = ["cat", "dog", "tac", "god", "act"]

result = {}

for w in words:
    key = ''.join(sorted(w))
    if key not in result:
        result[key] = []
    result[key].append(w)

for v in result.values():
    print(v)