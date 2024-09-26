import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    else:
        num = sys.argv[1]

        if int(num) % 2 != 0:
            print("I'm Odd.")
        else:
            print("I'm Even.")
except AssertionError as e:
    print(f"AssertionError: {e}")
except Exception as e:
    print("AssertionError: argument is not an integer")