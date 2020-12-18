values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values= [15, 10, 15, 20, 25, 30] 

def odds_sum(numbers):
    total = 0
  
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total

   

print(odds_sum(values))
print(odds_sum(other_values))

def greatest_number(numbers):
    greatest = numbers[0]

    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(greatest_number([1,2,3]))


print("--- more logic exercises---")

# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3


def smallest_number(numbers):
    smallest= numbers[0]
    for number in numbers:
        if number < smallest:
         smallest = number
    return smallest

print (smallest_number([1, 2, 3]))
print (smallest_number([3, 2, 1]))
print (smallest_number([4, 5, 4]))
print()

# Define a concatenate function that accepts a list of strings. 
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

def concatenate(words):
    total = ""
    for word in words:
        if len(word) > 2:
            total += word

    return total

print(concatenate(["abc", "def", "ghi"]))

print()

# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12
# 
#
def super_sum(letters):
    final= 0

    for letter in letters:
        if "s" in letter:
            index= letter.index("s")
            final+= index
    return final

print(super_sum(["mustache"]))
print(super_sum([""]))








    






