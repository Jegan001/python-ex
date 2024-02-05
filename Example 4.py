#Example 4: Python program to calculate the sum of all the odd numbers within the given range.
number =int(input("enter a number:"))
sum_even = 0
for i in range(1,number,2):
    print(i,end=" ")
    sum_even += i
print('sum_even:',sum_even)