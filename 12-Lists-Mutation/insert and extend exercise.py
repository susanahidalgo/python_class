# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# EXAMPLES
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def factors(value):
    my_factors = []
    
    for i in range(1, value + 1):
        if value % i == 0:
            my_factors.append(i)

    return my_factors

print(factors(2))
print(factors(10))
print(factors(64))


