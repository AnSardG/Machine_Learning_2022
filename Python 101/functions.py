"""
The reserved word for functions is "def"

The code below won't run since this is not a compiled language; this means
that the interpreter hasnt executed and stored the definition before calling it
** temperature_calculation(43, 12, 80) **
"""

def temperature_calculation(temperature, medium_temperature, humidity_percentage):
    """
    temperature = 43
    medium_temperature = 12
    humidity_percentage = 80
    """
    coefficient = 45 * 3.1416
    calculation = temperature * medium_temperature * humidity_percentage
    calculation = calculation / 7 * coefficient
    calculation = "The result is: " + str(calculation)
    print(calculation)

temperature_calculation(43, 12, 80)

"""
Now let's try functions that have a return value, since Python is 
both a Strongly and DYNAMICALLY typed language you don't have to specify the return data type of course
"""

def calculate_value(num1, num2):
    sum = num1 + num2
    return sum

print(calculate_value(2, 2))
"""
This is cool, you can return more than one value with a function this way
of course you dont have any problem naming the variables inside the function like
the "global" variables since their scope is locally adjusted to the function
"""
def calculate_sum_and_substraction(num1, num2):
    sum = num1 + num2
    substraction = num1 - num2
    return sum, substraction

num1 = 3
num2 = 2
# You can assign two variables at once like this from the return, makes total sense
sum, substraction = calculate_sum_and_substraction(num1, num2)
print ("The sum of",num1,"+",num2,"is:",sum)
print("The substraction of",num1,"-",num2,"is:",substraction)