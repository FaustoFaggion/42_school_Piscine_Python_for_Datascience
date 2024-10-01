import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    #IF INDEX 1 DON'T EXIST SYS REAISE IndexError
    num = sys.argv[1]
    #IF int() NOT RECEIVE A NOT INT VALUE RAISE THE ValueError
    if int(num) % 2 != 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")
except AssertionError as e:
    print(f"AssertionError: {e}")
except ValueError as e:
    print("AssertionError: argument is not an integer")
except IndexError as e:
    print("AssertionError: argument not provided")
except Exception as e:
    print(e)

print("Jorge")