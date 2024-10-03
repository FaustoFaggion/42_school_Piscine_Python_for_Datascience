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
    except Exception as e:
        print(e)

if __name__ == "__main__":
    aff_life()
