low = 1
high = 1000
guesses = 1

print("Please think of a number between {} and {}".format(low, high))
input("Press Enter to start")

while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? Please enter"
                     " h or l, or c if my guess was correct."
                     .format(guess).casefold())
    if high_low == "h":
        #guess higher
        low = guess + 1

    if high_low == "l":
        pass
        high = guess - 1

    if high_low == "c":
        print("AHA I KNEW IT In {} no less".format(guesses))
        break
    else:
        print("Please enter h, l or c")

        guesses = guesses + 1
else:
    print("You thought of the number {}!".format(low))
    print("I got it in {} tries!".format(guesses))