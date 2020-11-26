print(len("python"))
print(len("programming"))
print(len("sdfgajdierwaio5676543sasjdknvsaoijdsns"))

print("Susana " + "Hidalgo")

print("\n")


print("---EXERCISES LENGHT + BOOLEANS---")
print("\n")

# Define a long_word function that accepts a string. 
# The function should return a boolean that reflects 
# whether the string has more than 7 characthers.

def long_word(a=""):
    return len(a)>7

a= "Python"


print(long_word(a))

a= "magnificent"

print(long_word(a))



# Define a first_longer_than_second function that accepts two string arguments. 
# The function should return a True if the first string is longer than the second 
# and False otherwise (including if they are equal in length).

def first_longer_than_second(a="", b=""):
    return len(a)>len(b)
    return len(a)<=len(b)

a="python"
b="Ruby"

print(first_longer_than_second(a,b))

a="cat"
b="mouse"

print(first_longer_than_second(a,b))

a="Steven"
b="Seagal"

print(first_longer_than_second(a,b))


#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")     => True
# first_longer_than_second("cat", "mouse")       => False
# first_longer_than_second("Steven", "Seagal")   => False