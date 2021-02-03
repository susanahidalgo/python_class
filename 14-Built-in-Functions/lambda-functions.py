colors = ["black", "white", "yellow","magenta", "red", "blue"]

print(list(filter(lambda color: len(color)>5 , colors)))
print()

print(list(filter(lambda color: "y" in color, colors)))
print()

print(list(map(lambda color: color.count("i"), colors)))
print()

print(list(map(lambda color: color.replace("e", "$"), colors)))