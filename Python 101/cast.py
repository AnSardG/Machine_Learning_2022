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
int_as_boolean = bool(1)
print(int_as_boolean)
string_as_boolean = bool("Locura")
print(string_as_boolean)