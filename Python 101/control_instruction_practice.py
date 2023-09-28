"""
50 people and they want: 
70% ice-cream
20% pie
10% custard
"""

stock = input("Introduce the dessert: ")
if stock == "ice-cream":
    print("Remember buying the disposable spoons")
elif stock == "pie":
    print("Remember buying disposable plates")
elif stock == "custard":
    print("Remember buying caramel sauce")
else:
    print("This dessert is invalid")