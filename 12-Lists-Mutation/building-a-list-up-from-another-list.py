powerball_numbers= [4, 8, 15, 16, 23, 42]

def squares(numbers):
    squares= []
    for number in numbers:
        squares.append(number * number)
    return squares

print(squares(powerball_numbers))
print()

def convert_to_floats(numbers):
    floats= []
    for number in numbers:
        floats.append(float(number))
    return floats

print(convert_to_floats(powerball_numbers))
print()

def even_or_odd(numbers):
    results= []
    for number in numbers:
        if number % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    return results

print(even_or_odd(powerball_numbers))







