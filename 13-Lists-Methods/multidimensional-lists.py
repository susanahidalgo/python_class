bubble_tea_flavors=[
    ["Mango", "Mint", "Passion Fruit"],
    ["Peach", "Plum", "Watermelon","Cherry"],
    ["Kiwi", "Chocolate"]
]

print(len(bubble_tea_flavors))
print((bubble_tea_flavors)[0])
print()
print((bubble_tea_flavors)[1])
print()
print((bubble_tea_flavors)[2])

print(len(bubble_tea_flavors[2]))

print((bubble_tea_flavors[1][2]))
print((bubble_tea_flavors[0][1]))

print()

all_flavors = []

for flavor_pack in bubble_tea_flavors:
    for flavor in flavor_pack:
        all_flavors.append(flavor)

print(all_flavors)

