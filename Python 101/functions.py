"""
The reserved word for functions is "def"

The code below won't run since this is not a compiled language; this means
that the interpreter hasnt executed and stored the definition before calling it
** temperatureCalculation(43, 12, 80) **
"""

def temperatureCalculation(temperature, mediumTemperature, humidityPercent):
    """
    temperature = 43
    mediumTemperature = 12
    humidityPercent = 80
    """
    coefficient = 45 * 3.1416
    calculation = temperature * mediumTemperature * humidityPercent
    calculation = calculation / 7 * coefficient
    calculation = "The result is: " + str(calculation)
    print(calculation)

temperatureCalculation(43, 12, 80)

"""
Now let's try functions that have a return value, since Python is 
both a Strongly and DYNAMICALLY typed language you don't have to specify the return data type of course
"""

def calculateValue(num1, num2):
    sum = num1 + num2
    return sum

print(calculateValue(2, 2))
"""
This is cool, you can return more than one value with a function this way
of course you dont have any problem naming the variables inside the function like
the "global" variables since their scope is locally adjusted to the function
"""
def calculateSumAndSubstraction(num1, num2):
    sum = num1 + num2
    substraction = num1 - num2
    return sum, substraction

num1 = 3
num2 = 2
# So good that you can assign two variables at once like this from the return, makes total sense
sum, substraction = calculateSumAndSubstraction(num1, num2)
print ("The sum of",num1,"+",num2,"is:",sum)
print("The substraction of",num1,"-",num2,"is:",substraction)