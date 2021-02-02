# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0


def nested_sum(list_of_numbers):
    number= 0
    for nest in list_of_numbers:
        for value in nest:
            number += value 

    return number

print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]])  )

print()

# Define a fancy_concatenate function that accepts a list of lists of 
# strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if 
# the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

def fancy_concatenate(rows):
    total = ""
    for nest in rows:
        if len(nest) == 3:
                for word in nest:
                     total += word
               
            

    return total

print(fancy_concatenate([["A", "B", "C"]]) )
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])  )
            

        
            

    