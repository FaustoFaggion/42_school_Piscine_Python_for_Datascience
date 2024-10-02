import sys
from ft_filter import ft_filter

def f(x):
    if len(x) < 3:
       return True
    else:
       return False

def main(argv: any):

    try:
        assert len(argv) == 3, "AssertionError: the arguments are bad"
        assert argv[2].isdigit(), "AssertionError: the arguments are bad .."
        
        n = int(argv[2])
        text_to_list = argv[1].split()    
        words_lst: list = [x for x in text_to_list if x.isalpha()]
        response = ft_filter(lambda word: len(word) > n, words_lst)
   
        for x in response:
            print(x)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main(sys.argv)



    