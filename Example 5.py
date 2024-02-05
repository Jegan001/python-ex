#Example 5: Python program to print a multiplication table of a given number
table =input("which table do you want ? enter here: ")
print('MULTIPLICATION TABLE:')
x =10
for i  in range(x):
    for j  in table:
        mul = i*int(j)
    print(f"{i} *{j} ={mul}")