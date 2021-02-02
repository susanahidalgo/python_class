numbers = [3, 4, 5, 6, 7]

#squares=[]

#for number in numbers:
    #squares.append(number ** 2)

#print(squares)
#print(number)

squares=[number ** 2 for number in numbers]
print(squares)

rivers=["Amazonas", "Nilo", "Duero"]
print([len(river) for river in rivers])

expressions = ["LOL", "LMAO", "MDR"]

print([ expression.upper() for expression in expressions])


decimals = [4.95, 1.2, 4.4, 2,7]
print([ int(decimal) for decimal in decimals])
