#python Project
#First Display a menu
from ast import operator


print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

#input what the input enters
operation = input()

if operation == "1":
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The sum is " + str(int(num1) + int(num2)))

   
elif operation == "2":
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Difference is " + str(int(num1) - int(num2)))

elif operation == "3":
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The sum is " + str(int(num1) * int(num2)))

elif operation == "4":
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Remainder is " + str(int(num1) / int(num2)))

else:
    print('Invalid Entry')

