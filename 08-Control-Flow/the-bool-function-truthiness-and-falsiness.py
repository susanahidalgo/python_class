if 3:
    print("Hello")

if -1:
    print("It's me")

if 0:
    print("Adele")

if "Hello":
    print("Adele")

if "":
    print("The singer")

print("--ANOTHER BOOLEANS--")
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("lol"))
print()
print("--- EXERCISE ---")

# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2)    => "even"
# even_or_odd(0)    => "even"
# even_or_odd(13)   => "odd"
# even_or_odd(9)    => "odd"


def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    
    return "odd"

print(even_or_odd(2))
print(even_or_odd(0))
print(even_or_odd(13))
print(even_or_odd(9))






print()

# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is ______" 
# where the first space is the argument and the second space 
# is either 'truthy' or 'falsy'. See the sample invocations below.
# 
# truthy_or_falsy(0)        => "The value 0 is falsy"
# truthy_or_falsy(5)        => "The value 5 is truthy"
# truthy_or_falsy("Hello")  => "The value Hello is truthy"
# truthy_or_falsy("")       => "The value  is falsy"

def truthy_or_falsy(value):
    if bool(value):
        return f"The value {value} is truthy"

    return f"The value {value} is falsy"

print (truthy_or_falsy(0))
print (truthy_or_falsy(5))
print (truthy_or_falsy("Hello"))
print (truthy_or_falsy(""))













