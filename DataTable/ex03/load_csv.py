import sys
import pandas as pd
from time import sleep

def load(path: str):

    try:
        if path.endswith(".csv") == False:
            print("Incorrect format")
            return None
         
        dataframe = pd.read_csv(path)
        return dataframe
    except FileNotFoundError as e:
        print(e)
        return None
