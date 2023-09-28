num1 = 10
num2 = 5
# sum
print (num1 + num2)
# subtraction
print (num1 - num2)
# multiplication
print (num1 * num2)
# division
print (num1 / num2)
# integer division
print (num1 // 3)
# power
print (num1 ** num2)
# module
print (num1 % num2)
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# This will raise an error since the function "input" reads a
# string and you cannot substract two strings this way
print (num1 - num2)