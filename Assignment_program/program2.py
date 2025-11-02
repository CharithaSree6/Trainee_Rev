# Check Whether a String is Palindrome or Not.

string = input('Enter a string: ')

reverse_string = string[::-1]
if string == reverse_string:
    print('this is a palindrome')
else:
    print('this is not a palindrome')