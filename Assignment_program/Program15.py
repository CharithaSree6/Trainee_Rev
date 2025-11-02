# Check whether a number has consecutive 0’s in its binary equivalent.
num = int(input("Enter a number: "))
binary = bin(num)[2:]   # convert to binary

if "00" in binary:
    print("Yes, it has consecutive 0s")
else:
    print("No, it does not have consecutive 0s")

print("Binary:", binary)