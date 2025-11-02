# Remove all duplicated words from a given sentence.


sentence = "hello world hello python world"

words = sentence.split()        # split into words
unique = list(set(words))       # remove duplicates using set
result = " ".join(unique)       # join back into sentence

print(result)