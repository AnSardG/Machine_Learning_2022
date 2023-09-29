"""
 FOR LOOP:
 it starts with 0 if you dont specify the first iteration value
 and stops before reaching the integer passed as a parameter
"""
total = 0
for x in range(7):
    print("We're in the iteration number:", x)
    total += 5
    print("The total is:", total)
# Practice exercise with for loops
partMax = (int)(input("Please introduce the amount of participants: "))
print("The system will be configured to accept", partMax,
      "participants, from now on you can manage this exact number of participants and no more")
for part in range(partMax):
    inscription = ""
    while inscription != "y":
        name = input("Introduce your name: ")
        email = input("Introduce your email: ")
        print("Hi", name, "your email is", email,
              "do you want to confirm the inscription? (Y/N): ")
        inscription = input().lower()
        if inscription == "y":
            print("Thanks, your inscription is finished.")
        else:
            print("Operation cancelled.")
    print("Your participant number is:", part + 1)
print("Maximum capacity of participants reached.")

# This is another way of doing a for loop
for x in range(2, 20):
    print(x)

# And now the last way of doing a for loop, with the increment (the last parameter)
# note: in the last iteration, when X reaches 92 the increment wont be happening again like other languages
for x in range(2, 100, 10):
    print(x)

# WHILE LOOP, sometimes you can do an infinite while when you need something operating all the time
i = 0
while i < 100:
    print("Iteration number:", i)
    i += i//2+1

text = input("Introduce any input: ")
while text != "stop":
    text = input("Introduce another input, or \"stop\" to cancel this operation: ")