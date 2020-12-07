def positive_or_negative (number):
    if number > 0:
        return("Positive!")
    
    elif number<0:
        return ("Negative!")
    
    elif number == 0:
        return ("Neither! It's a zero")

print(positive_or_negative(5))
print(positive_or_negative(-2))
print(positive_or_negative(0))

def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "substract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return("I don't know what you want me to do!")

print(calculator("add", 3, 4))
print(calculator("substract", 3, 4))
print(calculator("multiply", 3, 4))
print(calculator("divide", 3, 4))
print(calculator("lol", 3, 4))

print()
print("---EXERCISE---")

# Declare a negative_energy function that accepts a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero.
# 
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0

def negative_energy(number):
    if number >=0:
        return number
    elif number < 0:
        return -1 * number
    

print(negative_energy(5))
print(negative_energy(10))
print(negative_energy(-5))
print(negative_energy(8))
print(negative_energy(0))

        







