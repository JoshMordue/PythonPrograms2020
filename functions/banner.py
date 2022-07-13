def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print the String that's entered and align to the center with "*"
    at the sides of the screen which are Denoted by the screen width
    variable.

    :param text: The text to print, if an asterisk is entered it will
    print "*" the length of the screen width. The default value will
    is no text.
    :param screen_width: The parameter for the width of the print,
    including for four "*" on either side.
    :raises ValueError: if the supplied string is too long to fit in the
    screenwidth
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))


    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


screen_width = int(input("Please enter your desired banner width: "))
banner_text("*", screen_width)
banner_text("Always look on the bright side of life...", screen_width)
banner_text("If life seems jolly rotten,", screen_width)
banner_text("There's something you've forgotten!", screen_width)
banner_text("And that's to laugh and smile and dance and sing,", screen_width)
banner_text()
banner_text("When you're feeling in the dumps,", screen_width)
banner_text("Don't be silly chumps,", screen_width)
banner_text("Just purse your lips and whistle - that's the thing!", screen_width)
banner_text("And... always look on the bright side of life...", screen_width)
banner_text("*", screen_width)




