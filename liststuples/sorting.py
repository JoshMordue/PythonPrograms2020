pangram = "the quick brown fox jumps over the lazy dog"

letter = sorted(pangram)

print(letter)

numbers = [2.3, 4.5, 8.7]

sorted_numbers = sorted(numbers)
print(sorted_numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",key=str.casefold)
print(missing_letter)

names = ["Josh", "Sally", "joanne", "Terry", "Eric"]

names.sort(key=str.casefold)
print(names)

