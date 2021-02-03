
print("--Exercise 1--")
print()

# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]


def greater_sum(numbers, values):
    total= []
    for number in numbers:
        if sum(numbers) > sum(values):
            return numbers
    else:
        return values

print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([4, 5], [2, 3, 6]))
print(greater_sum([1], []))

print()
print("--Exercise 2--")
print()


#Declare a sum_difference function that accepts two lists of numbers.
# It should return the difference between
#  the sum of values in the first list and the second list
#
# EXAMPLES
# sum_difference([1, 2, 3], [1, 2, 4]) => 6 - 7 => -1
# sum_difference([4, 5], [2, 3, 6])    => 9 - 11 => -2
# sum_difference([1], [])              => 1

def sum_difference(numbers, values):
    total= 0
    for number in numbers:
        total= sum(numbers) - sum(values)

    return total

print(sum_difference([1, 2, 3], [1, 2, 4]))
print(sum_difference([4, 5], [2, 3, 6]))
print(sum_difference([1], []))