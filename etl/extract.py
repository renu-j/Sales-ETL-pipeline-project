import pandas as pd
import os

# Folder where the CSV files are stored
data_folder = '../data'

def extract_data():
    """
    Extract all CSV files from the data folder and combine them into a single DataFrame.
    Returns:
        pandas.DataFrame: Raw combined data from all stores
    """
    # List all CSV files in the folder
    files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

    # Read each CSV into a DataFrame and store in a list
    df_list = [pd.read_csv(os.path.join(data_folder, f)) for f in files]

    # Concatenate all DataFrames into a single DataFrame
    raw_data = pd.concat(df_list, ignore_index=True)

    # Return raw data for further processing
    return raw_data
