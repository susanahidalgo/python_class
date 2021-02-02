animals = ["cat", "bear", "lion","donkey", "zebra"]

big_animals = [animal for animal in animals if len(animal)>3]
print(big_animals)

def is_long_animal(animal):
    return len(animal)>3

print(list(filter(is_long_animal, animals)))