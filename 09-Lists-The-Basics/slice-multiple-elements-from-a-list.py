print("programming"[3:6])

muscles = ["biceps", "triceps", "cuadriceps"]

print(muscles[1:3])
print(muscles[1:2])
print(muscles[0:])
print(muscles[2:])

print(muscles[-4:-2])
print(muscles[-3:])
print(muscles[-1:])

print(muscles[::2])
print()
print("---Exercise Slicing---")

# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#
# EXAMPLE:
# values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3)     => ["a", "b"]
# split_in_two(values, 4)     => ["c", "d", "e", "f"]
# split_in_two(values, 1)     => ["a", "b"]
# split_in_two(values, 10)    => ["c", "d", "e", "f"]


def split_in_two(argument, number):
    if number % 2 == 0:
        return argument [2:] 
    else:
        return argument[0:2] 

argument=["a", "b", "c", "d", "e", "f"]

print (split_in_two(argument, 3))
print (split_in_two(argument, 4))
print (split_in_two(argument,1))
print (split_in_two(argument, 10))
print()
print("---more listing exercises---")



print()

# Declare a beginning_and_end function that accepts a list of elements.
#
# It should return True if the first and last elements in the list are equal and False if they are unequal.
#
# Assume the list will always have at least 1 element.
#
# beginning_and_end([1, 2, 3, 1])     => True
# beginning_and_end([1, 2, 3, 4, 5])  => False
# beginning_and_end(["a", "b", "a"])  => True
# beginning_and_end([15])             => True


def beginning_and_end(things):
    if things [0] == things [-1]:
        return True
    else:
        return False
   
      
things=[1, 2, 3, 1]
print(beginning_and_end(things))
things=[1, 2, 3, 4, 5]
print(beginning_and_end(things))
things= ["a", "b", "a"]
print(beginning_and_end(things))
things=[15]
print(beginning_and_end(things))
print()

# Declare a long_word_in_collection function that accepts a list and a string. 
# The function should return True if 
#   - the string exists in the list AND
#   - the string has more than 4 characters.
#
# words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")  => True
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False

def long_word_in_collection(stuff, dings):
    if dings in stuff and len(dings)>4:
        return True
    else:
        return False

stuff= ["cat", "dog", "rhino"]
print(long_word_in_collection(stuff, "rhino"))
print(long_word_in_collection(stuff, "cat"))
print(long_word_in_collection(stuff, "monkey"))


