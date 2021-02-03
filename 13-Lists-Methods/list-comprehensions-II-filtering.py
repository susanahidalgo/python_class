print(["abcdefghijklmnopqrstuvwxyz".index(word) for word in "donut"])
print()

print([number/2 for number in range(20)])

print()

donuts = ["Chocolate Cream", "Glassed", "Oreo Cream", 
"Cherry", "Jelly"]

#creamy_donuts = []

#for donut in donuts:
    #if "Cream" in donut:
        #creamy_donuts.append(donut)

#print(creamy_donuts)

creamy_donuts = [donut for donut in donuts if "Cream" in donut]
print(creamy_donuts)
print()

print([len(donut) for donut in donuts if "Cream" in donut])

print()

print([donut.split(" ")[0] for donut in donuts if "Cream" in donut])
