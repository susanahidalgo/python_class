#Define a fizzbuzz function that accepts a single number as an argument. The function should print every number from 1 to that argument. 
#There are a couple caveats.
#If the number is divisible by 3, print "Fizz" instead of the number.
#If the number is divisible by 5, print "Buzz" instead of the number.
#If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.
#If the number is not divisible by either 3 or 5, just print the number.


def fizzbuzz(number):
    cycle= 0
    while cycle<= 29:
        cycle += 1
        #print(cycle)
    
        if cycle % 3 == 0:
            print("Fizz")
        elif cycle % 5 == 0:
            print("Buzz")
        elif cycle % 3 == 0 and cycle % 5==0:
            print("Fizzbuzz")
        else:
            print(cycle)

print(fizzbuzz(30))
print ("hannes:")
fizzbuzz(3)
print()
print("------ANOTHER THING-------")
print()









