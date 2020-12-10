def fizzbuzz(number):
    if number % 15== 0:
        print("FizzBuzz")
    elif number % 5== 0:
        print("Buzz")

    elif number % 3== 0:
        print("Fizz")
    else:
        print(number)
    


def fizzbuzz_while(number):
    cycle= 1
    while cycle <= number:
        fizzbuzz(cycle)
        cycle +=1

fizzbuzz_while(24)
