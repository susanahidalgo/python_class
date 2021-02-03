numbers = [1, 2, 3, 4, 5, 6]

cubes = [number ** 3 for number in numbers]

print(cubes)

print()

def cube(number):
    return number ** 3

print(list(map(cube, numbers)))
print()

animals = ["cat", "bear", "lion","donkey", "zebra"]

print(list(map(len, animals)))
print()

print([len(animal) for animal in animals])
print()

