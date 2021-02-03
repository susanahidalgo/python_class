alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet[0:10:2])

print(alphabet[:26:3])
print(alphabet[::3])
print(alphabet[-20:-8:5])
print(alphabet[::-3])

print("\n")

print("---Exercises String Slicing---")
print("\n")

# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty")   => "dyn"
# first_three_characters("empire")    => "emp"

def first_three_characters(word):
    return word[0:3]

word="dynasty"

print(first_three_characters(word))

word="empire"

print(first_three_characters(word))

# Define a last_five_characters function that accepts a string argument. 
# The function should return the last 5 characters of the string.
#
# EXAMPLES:
# last_five_characters("dynasty")   => "nasty"
# last_five_characters("empire")    => "mpire"


def last_five_characters(word):
    return word[-5:]

word="dynasty"

print(last_five_characters(word))

word="empire"

print(last_five_characters(word))

# Define a is_palindrome function that accepts a string argument. 
# The function should return True if the string is spelled 
# the same backwards as it is forwards. 
# Return False otherwise.
#
# EXAMPLES:
# is_palindrome("racecar")   => True
# is_palindrome("yummy")     => False

def is_palindrome(word):
    word == word [::-1] 

word="racecar"

print(is_palindrome(word))


word="yummy"

print(is_palindrome(word))

















