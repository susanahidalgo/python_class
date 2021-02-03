mountains = ["Mount Everest", "Teide"]
print(mountains)
print()

mountains.extend(["Denali", "Alps", "K2"])
print(mountains)
print()

extra_mountains= ["Aconcagua", "Kilimanjaro", "Eiger"]
mountains.extend(extra_mountains)
print(mountains)
print()

burgers= ["Big Mac", "Long Crispy"]
more_burgers = ["Crispy Bun", "Union"]

my_meal = burgers + more_burgers
print(my_meal)
print()

burgers = burgers + more_burgers
print(burgers)