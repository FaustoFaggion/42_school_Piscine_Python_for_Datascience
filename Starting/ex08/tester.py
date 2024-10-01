from Loading import ft_tdqm
from time import sleep
from tqdm import tqdm


def main():

    for elem in tqdm(range(333)):
        sleep(0.005)
    
    for elem in ft_tdqm(333):
        sleep(0.05)

    return 0


if __name__ == "__main__":
    main()
