# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

vowels = frozenset("aeiou")
checked_input = input("Hello World ").lower()

finalSet = set(checked_input).difference(vowels)
print(finalSet)

print(sorted(finalSet))

finalSet = set(checked_input).difference(vowels)