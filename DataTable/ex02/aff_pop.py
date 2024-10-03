import sys
from DataTable.ex00.load_csv import load

def aff_pop():
    path = sys.argv[1]
    data_frame = load(path)
    print(data_frame)

if __name__ == "__main__":
    aff_pop()