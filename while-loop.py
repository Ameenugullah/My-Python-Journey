#while loop = this execute code WHILE some condition remains true.

name = input("Please enter your name: ")
while name == "":
    print("Name cannot be empty ")
    name = input("Please enter your name: ")
print(f"Hello {name}")

#age = input("Please enter your age: ")
#while age < 0:
#   print("Age cannot be negative ")
#  age = int(input("Please enter your age: "))
#print(f"You are {age} years old")

gender = input("Enter gender: ")
while gender == "":
    print("Gender cannot be empty ")
    gender = input("Enter gender: ")
print(f"You are a {gender}")


# Let's try logical operations

food = input("Please type your order (q to quit): ")
while food == "q":
    print(f"your order is {food}")
    food = input("Please type what else you want (q to quit): ")
    print("bye")
