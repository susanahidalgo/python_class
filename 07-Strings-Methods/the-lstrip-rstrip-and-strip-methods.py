empty_space="                content             "

print(empty_space.rstrip())
print(len(empty_space.rstrip()))

print(empty_space.lstrip())
print(len(empty_space.lstrip()))


print(empty_space.strip())


website="www.python.org"
print(website.lstrip("w"))
print(website.rstrip("org"))
print(website.strip(".worg."))

print()
print("--- Exercise Cleaning Up")
print()

# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument. It should also replace every occurrence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).
#
# fancy_cleanup("       geronimo crikey  ")   => "zeronimo!crikey"
# fancy_cleanup("       nonsense  ")          => "nonsense"
# fancy_cleanup("grade")                      => "zrade"


def fancy_cleanup(word):
    return word.strip().replace("g","z").replace(" ", "!")

print(fancy_cleanup("       geronimo crikey  "))
print(fancy_cleanup("       nonsense  "))
print(fancy_cleanup("grade"))


