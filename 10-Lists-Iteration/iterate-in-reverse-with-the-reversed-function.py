the_simpsons = ["Homer", "Marge", "Lisa", "Bart", "Maggie"]

for character in the_simpsons[::-1]:
    print(f"{character} has a total of {len(character)} characters")

print()
print(reversed(the_simpsons))
print(type(reversed(the_simpsons)))
print()
for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters")
