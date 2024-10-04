# Necessary packages:
# # pip install matplotlib

import sys
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Specify the interactive backend $sudo apt-get install python3-tk
import matplotlib.pyplot as plt
from DataTable.ex00.load_csv import load

def aff_life():
    
    try:
        #CREATE DATA FRAME
        file_path = sys.argv[1]
        data_frame = load(file_path)
    
        #SET INDEX TO SEACH BY COUNTRY
        data_frame.set_index('country', inplace=True)
        
        #CREATE A SERIES WITH A SPECIFIC COUNTRY
        my_country = "Brazil"
        df_my_country = data_frame.loc[my_country]

        #SPECIFY X AND Y AXIS
        x_axis = df_my_country.index
        y_axis = df_my_country.values

        #PLOT SELECTED TABLE VALUES
        # df_my_contry = df_my_contry.transpose()
        # plt.figure(figsize=(12, 6))
        plt.plot(x_axis, y_axis)
        
        #SET LABELS
        # df_title = f"{my_country} Life expectancy projections"
        # df_xlabel = "Year"
        # df_ylabel = "Life expectancy"
        # df_my_country.plot(xlabel = df_xlabel, ylabel = df_ylabel, title = df_title)
        plt.title(f"{my_country} Life expectancy projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        
        # SET LAYOUT
        plt.legend()
        plt.tight_layout()  

        # SET X-TICKS To SHOW EVERY 40 YEARS
        ticks = range(0, len(x_axis), 40)
        plt.xticks(ticks, labels=x_axis[::40], rotation=45)

        #  SHOW CHART IN THE TERMINAL
        plt.show()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    aff_life()
