import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def color_print(text: str, *effects: str) -> None:
    """
    print text using the ANSI sequences to chance colour etc
    :param text: the text to print
    :param effects: the effect we want. one of the constants defined
    at the start of this module
    """
    effect_string = "".join(effects)

    text = "{0}{1}{2}".format(effect_string, text, RESET)
    print(text)



colorama.init()
color_print("TEST", GREEN)
color_print("TEST RED IN BOLD", RED, BOLD)
color_print("Test")
color_print("Test", BLUE)
color_print("Test", BLUE, REVERSE)
color_print("Test", YELLOW)
color_print("Test", YELLOW, BOLD)
color_print("Test", BLUE, REVERSE, UNDERLINE)



colorama.init()
