from ft_calculator import Calculator

def main():

    try:
        c1 = Calculator

        lst1 = [2, 4, 1]
        lst2 = [3, 4, 1]
        c1.dotproduct(lst1, lst2)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()