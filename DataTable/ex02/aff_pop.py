import sys
import matplotlib
matplotlib.use('TkAgg')  # Specify the interactive backend $sudo apt-get install python3-tk
import matplotlib.pyplot as plt
from DataTable.ex00.load_csv import load

def data_parse(value):
    

    if str(value).endswith("M"):
        new_value = str(value).strip('M')
        new_value = float(new_value) * 1000000
        return int(new_value)
    elif str(value).endswith("k"):
        new_value = str(value).strip("k")
        new_value = float(new_value) * 1000
        return int(new_value)
    return value

def aff_pop():
    try:
        #CREATE DATA FRAME
        file_path = sys.argv[1]
        data_frame = load(file_path)
        
        #SET INDEX TO SEARCH BY COUNTRY
        data_frame.set_index("country", inplace=True)
        
        #PARSE VALUES
        columns_to_parse = data_frame.loc[:, "1800":].columns
        print(columns_to_parse)
        data_frame[columns_to_parse] = data_frame[columns_to_parse].map(data_parse)

        # #CREATE FILTERED DATA FRAME
        my_country = "Brazil"
        other_country = "Angola"
        df_my_country = data_frame.loc[my_country]
        df_other_country = data_frame.loc[other_country]

        # #SPECIFY X AND Y AXIS
        x_axis = df_my_country.index        
        y_my_axis = df_my_country.values
        y_other_axis = df_other_country.values
        
        #PLOT DATA FRAME
        plt.plot(x_axis, y_my_axis, label= my_country)
        plt.plot(x_axis, y_other_axis, label= other_country)

        # #SET LABELS
        # plt.legend(loc='upper left')  # or any other location
        df_title = "Populations Projection"
        df_xlabel = "Year"
        df_ylabel = "Population"
        df_my_country.plot(xlabel = df_xlabel, ylabel = df_ylabel, title = df_title)
        # plt.title = "Populations Projection"
        # plt.xlabel = "Year"
        # plt.ylabel = "Popupation"
        
        # Step 6: Set x-ticks to show every 4 years
        ticks = range(0, len(x_axis), 40)
        plt.xticks(ticks, labels=x_axis[::40], rotation=45)

        #  SHOW CHART IN THE TERMINAL
        plt.legend()
        plt.tight_layout()  
        plt.show()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    aff_pop()