print ("fast" in "Breakfast") 
print ("fast" in "dinner")

meals= ["breakfast", "lunch", "dinner"]
print("lunch" in meals)

print()

test_scores=[99.0, 87.4, 90.15]
print(99.0 in test_scores)
print(99 in test_scores)
print(28 in test_scores)
print()
print("--not in--")
print(23 not in test_scores)
print("dinner" not in meals)

if 99 in test_scores:
    print("Lol, this is funny")
if 23 not in test_scores:
    print("Well, it doesn't matter that much")