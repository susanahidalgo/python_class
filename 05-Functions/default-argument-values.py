def add(a=0, b=0):
    return a+b

print(add(7,8))

print(add(10))

print(add())


#Define a string_adder function that accepts two strings (a and b) as arguments.

def string_adder(a="",b=""):
    return (a+ " " +b)

print (string_adder("lol", "that's funny"))
print ("-----Hello World ----")
print(string_adder("Hello", "World"))
print("emilio estevez: "+string_adder("Emilio", "Estevez"))
print(string_adder())



# It should return a concatenated version of the arguments with a space in between.
# If the user does not pass in arguments, both arguments should default to an empty string.
#
# EXAMPLES
# string_adder("Hello", "World")      => "Hello World"
# string_adder("Emilio", "Estevez")   => "Emilio Estevez"
# string_adder()                      => " "
# string_adder("Tiger")               => "Tiger "


 #Define a multiplier function that accepts three integers as arguments.
# Return the product of the arguments. The product is the total when values are multiplied together.
# If the user does not provide any arguments, all three parameters should have default arguments of 1.
#
# EXAMPLES
# multiplier(2, 2, 2)    => 8
# multiplier()           => 1
# multiplier(3)          => 3
# multiplier(2, 5)       => 10


def multiplier(a=1,b=1,c=1):
    return a*b*c


print ("I want the multiplication of 2, 2 and 2: "+str(multiplier(2,2,2)))
print (multiplier())
print (multiplier(3))
print (multiplier(2, 5))

    









