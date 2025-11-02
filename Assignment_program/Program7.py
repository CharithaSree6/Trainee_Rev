# Split String into Equal Parts

string = "abcdefgh"
n = 2

if len(string) % n != 0:
    print("String length is not divisible by", n)
else:
    parts = []
    for i in range(0, len(string), n):
        part = string[i:i+n]
        parts.append(part)

    print("Equal parts:", parts)