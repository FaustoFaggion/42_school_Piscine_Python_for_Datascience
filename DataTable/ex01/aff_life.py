# Necessary packages:
# # pip install matplotlib

import sys
import pandas as pd
# import matplotlib
# matplotlib.use('TkAgg')  # Specify the interactive backend
import matplotlib.pyplot as plt
from DataTable.ex00.load_csv import load

def aff_life():
    file_path = sys.argv[1]
    # data_frame = load(file_path)

    # Optional: Print the DataFrame to check its content
    # print(data_frame)
    # Plot the DataFrame
    # data_frame.plot()
    x = [1, 2, 3, 4]
    y = [3, 4, 5, 6]
    plt.plot(x, y)  # Show the 
    # plt.show()
    return 0

if __name__ == "__main__":
    aff_life()
