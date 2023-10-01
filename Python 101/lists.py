"""
As we see lists can contain varied data types since Python is a
dinamically typed language, so there's no problem creating a lists
as follows
"""
flavours = ["chocolate","american cream","vanilla", True, 10,12.3]
print("All flavours:",flavours)
print("First flavour:",flavours[0])

"""
Pop method returns the data/object in the position passed 
as an argument and then removes it from the list
"""
print("Removing:",flavours.pop(0))
print("All flavours:",flavours)
# This way you can add anything at the end of a list
flavours.append("Coco")
flavours.append("Last flavour")
"""
This is the method in Python to get the length of a container of items
you have to be careful since the length gives the actual number of parameters,
but when you are searching the index you should substract 1 to get the last item.
"""
print(flavours[len(flavours) - 1])
"""
With the insert method you can add in the specified index an object,
a really good thing of this method is that you don't have to make
space or move items by yourself, it does everything, moves the items
to the right or left and then introduces your item in the specified
index
"""
print(flavours)
print("Adding chocolate flavour to the middle of the list")
flavours.insert((len(flavours) - 1) // 2, "Chocolate")
print(flavours)
# Now let's try working with a couple of lists and merging them
flavours = ["Chocolate", "Vanilla"]
flavours2 = ["American cream", "Coco"]
"""
The method "extends" uses the iterator of the list to append those
elements to the list that's being extended
"""
flavours.extend(flavours2)
print(flavours)
flavours.append("Chocolate")
"""
Method to remove the first ocurrence of the value passed as parameter 
from this list
"""
flavours.remove("Chocolate")
print(flavours)