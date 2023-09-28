# For loop, it starts with 0 and stops before reaching
# the integer passed as a parameter
total = 0
for x in range(7):
    print("We're in the iteration number:",x)
    total += 5
    print("The total is:",total)
# Practice exercise with for loops
partMax = (int)(input("Please introduce the amount of participants: "))
print ("The system will be configured to accept",partMax,"participants, from now on you can manage this exact number of participants and no more")
for part in range(partMax):
    inscription = ""
    while inscription != "y":
        name = input("Introduce your name: ")
        email = input("Introduce your email: ")
        print("Hi",name,"your email is",email,"do you want to confirm the inscription? (Y/N): ")
        inscription = input().lower()        
        if inscription == "y":
            print("Thanks, your inscription is finished.")
        else:
            print("Operation cancelled.")
    print("Your participant number is:",part + 1)
print("Maximum capacity of participants reached.")