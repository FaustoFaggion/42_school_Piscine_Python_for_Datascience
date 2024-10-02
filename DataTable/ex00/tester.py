import sys
from load_csv import load

def tester():
    
    try:
        data_frame = load(sys.argv[1])
        print("You are loading a data frame o dimensions", end=" ")
        print(data_frame.shape)
        print(data_frame)
        # display(dataframe)
    except Exception as e:
        print(e)
        return None
if __name__ == "__main__":
    tester()    