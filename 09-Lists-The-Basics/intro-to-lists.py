empty= []
empty = list()

sodas = ["Coke", "Pepsi", "Dr.Pepper"]
print(len(sodas))

quarterly_revenues= [1500, 1200, 1000, 980]
print(len(quarterly_revenues))

user_settings= [True, False, True, True]
print(len(user_settings))
print()
print("---Exercise Lists---")

# Create an empty list and assign it to the variable "empty".
empty= []

# Create a list with a single Boolean — True — and assign it to the variable "active".
active = [True]

# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".
favorite_number= [1, 4, 7, 9, 6]

# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".
colors= ["red", "green", "blue"]

# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise
def is_long(elements):
    return len(elements) > 5
   

elements = [1, 4, 6, 34, 7, 35, 3]
print(is_long(elements))





