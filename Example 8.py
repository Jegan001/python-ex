#Example 8: Python program to check if the given string is a palindrome.
s = input("enter your string to find palindrme or not:")
p =[]
for  i in s:
    reverse=s[::-1]
if reverse==s:
    print(s,"is palindrome")
else:
    print(s,"is not a palindrome")