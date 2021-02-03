pizzas = [
    "mushroom", "pepperoni", "cheese", "paprika",
    "cheese", "tomato"]

print(pizzas.index("cheese"))
print(pizzas.index("tomato"))
print(pizzas.index("paprika"))

if "olive" in pizzas:
    print(pizzas.index("olive"))

print(pizzas.index("cheese", 3))
