from ft_calculator import Calculator

def main():

    try:
        lst1 = [5, 10, 2]
        lst2 = [2, 4, 3]
        Calculator.dotproduct(lst1, lst2)
        Calculator.add_vec(lst1, lst2)
        Calculator.sous_vec(lst1, lst2)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()