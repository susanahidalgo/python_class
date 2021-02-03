fruits = ["Lemon", "Orange", "Lime"]

fruits.clear()
print(fruits)



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

print(push_or_pop([10]))  
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))

    