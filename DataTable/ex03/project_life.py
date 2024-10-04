from DataTable.ex03.load_csv import load
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def data_parse(value):
    

    if str(value).endswith("M"):
        new_value = str(value).strip('M')
        new_value = float(new_value) * 1000000
        return float(new_value)
    elif str(value).endswith("k"):
        new_value = str(value).strip("k")
        new_value = float(new_value) * 1000
        return float(new_value)
    elif pd.isna(value):
        new_value = 0.0
        return float(new_value)
    return float(value)

def project_life():

    try:
       #CREATE DATA FRAME
        df1_file_path = "DataTable/ex03/income.csv"
        df2_file_path = "DataTable/ex03/life_expectancy_years.csv"
        df_1 = load(df1_file_path)
        df_2 = load(df2_file_path)
        
        #SET INDEX TO SEARCH BY COUNTRY
        df_1.set_index("country", inplace=True)
        df_2.set_index("country", inplace=True)
        
        #PARSE VALUES
        df1_columns_to_parse = df_1.loc[:, "1800":].columns
        df2_columns_to_parse = df_2.loc[:, "1800":].columns
        df_1[df1_columns_to_parse] = df_1[df1_columns_to_parse].map(data_parse)
        df_2[df2_columns_to_parse] = df_2[df2_columns_to_parse].map(data_parse)
        # print(df_1)
        # print(df_2)

        # MERGE DATA FRAMES
        df_merge = df_1.merge(df_2, on='country', suffixes=("df_1", "df_2"))
        print(df_merge)
        # #CREATE FILTERED DATA FRAME
        # year = "1900"
        # other_country = "Angola"
        # df_my_country = df_1.loc[:, year]
        # df_other_country = data_frame.loc[other_country]

        # #SPECIFY X AND Y AXIS
        x_axis = df_merge["1900df_1"]     
        y_my_axis = df_merge["1900df_2"]
        # y_other_axis = df_other_country.values
        
        #PLOT DATA FRAME
        plt.scatter(x_axis, y_my_axis, color='blue', label='country')

        # #SET LABELS
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life expectancy')
        plt.title('1900')
        
        # Step 6: Set x-ticks to show every 4 years
        # ticks = range(0, len(x_axis), 100)
        # plt.xticks(ticks, labels=x_axis[::100], rotation=45)

        #  SHOW CHART IN THE TERMINAL
        plt.legend()
        plt.tight_layout()  
        plt.show()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    project_life()