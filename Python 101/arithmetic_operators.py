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
# This way will work by casting the data type after reading
# the input, obviously as long as the type can be converted
num1 = (int)(input("Enter a number: "))
num2 = (int)(input("Enter another number: "))
print (num1 - num2)