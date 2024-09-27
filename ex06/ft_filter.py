import sys
from filterstring import filterstring

def f(x):
    if x < 4:
       return True
    else:
       return False

def main(argv: any):
    
    try:
        if len(argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        if not argv[2].isdigit():
            raise AssertionError("AssertionError: the arguments are bad ..")
    
        n = argv[2]
        text = argv[1].split()
        for word in text:
             if not word.isalpha():
                raise AssertionError("AssertionError: the arguments are bad .")
        
        response = filterstring(text, n)
   
        for x in response:
            print(x)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main(sys.argv)