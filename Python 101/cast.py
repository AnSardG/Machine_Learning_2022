# Casting variables to their respective data types
integer = int("777")
print(type(integer)) 
"""
This raises an error since you cannot cast to int a decimal string

   integer = int("777.3")
   print(type(integer))
"""
decimal = float("4.3")
print(type(decimal))
boolean = bool("True")
print(type(boolean))
booleanAsInt = int(True)
print(booleanAsInt)
intAsBoolean = bool(1)
print(intAsBoolean)
stringAsBoolean = bool("Locura")
print(stringAsBoolean)