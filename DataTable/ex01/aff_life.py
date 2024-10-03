# Necessary packages:
# # pip install matplotlib

import sys
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Specify the interactive backend $sudo apt-get install python3-tk

import matplotlib.pyplot as plt
from DataTable.ex00.load_csv import load

def aff_life():
    file_path = sys.argv[1]
    data_frame = load(file_path)
    # print("\ndataframe:\n", data_frame)
    # print("\ndataframe.at:\n", data_frame.at["Angola", "1800"])
    # print("\ndataframe.attrs:\n", data_frame.attrs)
    # print("\ndataframe.axes:\n", data_frame.axes)
    # print("\ndataframe.columns:\n", data_frame.columns)
    # print("\ndataframe.dtypes:\n", data_frame.dtypes)
    # print("\ndataframe.index:\n", data_frame.index)
    
    #GET VALUES FROM A SPECIFIC COUNTRY
    data_frame.set_index('country', inplace=True)
    my_country = "Brazil"
    df_my_contry = data_frame.loc[my_country]
    
    #SPECIFY X AND Y AXIS
    x_axis = df_my_contry.index
    y_axis = df_my_contry.values

    #PLOT SELECTED TABLE VALUES
    # df_my_contry = df_my_contry.transpose()
    plt.figure(figsize=(12, 6))
    plt.plot(x_axis, y_axis)
    
    #SET LABELS
    plt.title = f"{my_country} Life expectancy projections"
    plt.xlabel = "Year"
    plt.ylabel = "Life expectancy"
    
    # Step 6: Set x-ticks to show every 4 years
    ticks = range(0, len(x_axis), 40)
    plt.xticks(ticks, labels=x_axis[::40], rotation=45)

    #  SHOW CHART IN THE TERMINAL
    plt.show()
    
    # Optional: Print the DataFrame to check its content
    # print(data_frame)
    # Plot the DataFrame
    # plt.title("Brazil Life Expectancy Projections")
    # plt.xlabel("year")
    # plt.ylabel("Life expectancy")
    return 0

if __name__ == "__main__":
    aff_life()
