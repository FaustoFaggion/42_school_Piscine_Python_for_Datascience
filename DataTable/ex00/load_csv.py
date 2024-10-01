import sys
import pandas as pd

def load(path: str):

    try:
        if path.endswith(".csv") == False:
            print("Incorrect format")
            return None

        dataframe = pd.read_csv(path)
        print(dataframe)
        # display(dataframe)
    except FileNotFoundError as e:
        print(e)
        return None
if __name__ == "__main__":
    load(sys.argv[1])