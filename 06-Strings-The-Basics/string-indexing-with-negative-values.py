

print("----INDEXING EXERCISE----")

print("\n")

# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#

def same_first_and_last_letter(word):
    return word[0] == word[-1]
    
 
word= "runner"

print(same_first_and_last_letter(word))

word= "Runner"


print(same_first_and_last_letter(word))



# EXAMPLES:
# same_first_and_last_letter("runner")   => True
# same_first_and_last_letter("Runner")   => False
# same_first_and_last_letter("clock")    => False
# same_first_and_last_letter("q")        => True


# Define a three_number_sum function that accepts a 3-character string as an argument. 
# The function should add up the sum of the digits of the string. 
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.

def three_number_sum (a="",b="",c=""):
    return (a+b+c)

a=int("1")
b=int("2")
c=int("3")

print(three_number_sum(a,b,c))

def three_number_sum (a="",b="",c=""):
    return (a+b+c)

a=int("5")
b=int("6")
c=int("7")


print(three_number_sum(a,b,c))

def three_number_sum (a="",b="",c=""):
    return (a+b+c)

a=int("4")
b=int("4")
c=int("4")


print(three_number_sum(a,b,c))
#
# EXAMPLES:
# three_number_sum("123")   => 6
# three_number_sum("567")   => 18
# three_number_sum("444")   => 12
# three_number_sum("000")   => 0





