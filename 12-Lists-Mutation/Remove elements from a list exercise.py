# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element 
# added to the new list
# Assume the order of numbers in the argument will 
# never require removing from an empty list
#
# EXAMPLES
# push_or_pop([10])            => [10]
# push_or_pop([10, 4])         => []
# push_or_pop([10, 20, 30])    => [10, 20, 30]
# push_or_pop([10, 20, 2, 30]) => [10, 30]

def push_or_pop(numbers):
    total = []
    for number in numbers:
        if number > 5:
            total.append(number)
        else:
            total.pop()
    
    return total




# Declare a delete_all function that accepts a list of strings 
# and a target string
# Remove all occurrences of the target string from the list and return it
#
# EXAMPLES
# delete_all([1, 3, 5], 3)  => [1, 5]
# delete_all([5, 3, 5], 5)  => [3]
# delete_all([4, 4, 4], 4)  => []
# delete_all([4, 4, 4], 6)  => [4, 4, 4]

def delete_all(items, target):
    
    while target in items:
        items.remove(target)
    
    return items
    
print(delete_all([1, 3, 5], 3))