print("Hello World!")
print("Hello Again")
print("I Like Typing This")
print("This Is Fun")
print('Yay! Printing')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')
print("-----------------------------------")
print("I Love Python Programming Language.")

#A comment. this is so you can read your program later.
#Anything after the # is ignored by python.
print("I could have code like this.") # and the comment after is ignored
# You can also use a comment to "disable" or comment out code
# print("this wont run")
print("this will run.")
print("-----------------------------")

print("I will now count my chickens:")
#this will calculate my  hens
print("Hens", 25 + 30 / 6)
#this will calculate my rooters
print("Roosters", 100 - 25 * 3 % 4)
#i will count the total eggs
print("Now i will count the eggs:")
print(float(3 + 2 + + 1 - 5 + 4 % 2 - 1 / 4 + 6))
# calculating on booleans values
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)
print("Oh, thats why it's False.")
print("How about some more.")
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
print("-----------------------------")

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven =cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("we need to put about", average_passengers_per_car, "in each car.")
print("-----------------------------")

name = 'Chukwu .A. Chiemela'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inches_to_cm = 2.54
pound_to_kg = 0.453592

centimeters = height * inches_to_cm
kilograms = weight * pound_to_kg

print(f"Lets talk about {name}.")
print(f"He's {centimeters} centimeters tall. ")
print(f"He's {kilograms} kilogram heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"if i add {age}, {height}, and {weight}, I get {total}.")
print("-----------------------------")

types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")
hilarious = False
joke_evaluation = "isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
w = "This is the left side of...."
e = "a string with the right side."
print(w + e)

