print("---list comprehensions exercises---")
print()

# Uncomment the commented lines of code below and complete the list 
#comprehension logic

# The floats variable should store the floating point values 
# for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]

floats = [ float(value) for value in values]
print (floats)
print()

# The letters variable should store a list of 5 strings. 
# Each of the strings should be a character from 
# name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Boris"
letters = [ letter * 3 for letter in name]
print(letters)
print()

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = [len(element) for element in elements]
print (lengths)
print()

print("---destroying list exercise---")
print()

# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first
# list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]

def destroy_elements(numbers, values):
    return [number for number in numbers if number not in values]
            


print(destroy_elements([1, 2, 3], [1, 2]))
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]))

        