import sys

def main(argv: any):

    upper_letters = 0
    lower_letters = 0
    puctuation_marks = 0
    spaces = 0
    digits = 0

    try:
        if len(argv) < 2 or argv[1] == "":
            raise AssertionError("please provide a string")
        if len(argv) > 2:
            raise AssertionError("more than one argument is provided")
        
        word = argv[1]
        for char in word:
            if char.isupper():
                upper_letters = upper_letters + 1
            elif char.islower():
                lower_letters = lower_letters + 1
            elif char.isspace():
                spaces = spaces + 1
            elif char.isdigit():
                digits = digits + 1
            elif char.isascii():
                puctuation_marks = puctuation_marks + 1

        print(upper_letters, "upper letters")
        print(lower_letters, "lower letters")
        print(puctuation_marks, "punctuation marks")
        print(spaces, "spaces")
        print(digits, "digits")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main(sys.argv)