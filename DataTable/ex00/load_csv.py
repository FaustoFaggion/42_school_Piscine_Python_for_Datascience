import sys
import pandas as pd
from time import sleep

def load(path: str):

    try:
        if path.endswith(".csv") == False:
            print("Incorrect format")
            return None

        yield print("You are loading a data frame o dimensions", end=" ") 
        dataframe = pd.read_csv(path)
        yield print(dataframe.shape)
        print(dataframe)
        # display(dataframe)
    except FileNotFoundError as e:
        print(e)
        return None
if __name__ == "__main__":
    
    generator = load(sys.argv[1])
    for message in generator:
        print(message)