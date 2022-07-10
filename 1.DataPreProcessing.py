from optparse import Values
from utils import *
import pandas as pd
import numpy as np


data_csv_path = os.path.join(DATA_PATH, 'train.csv')
test_csv_path = os.path.join(DATA_PATH, 'test.csv')
tempdir = os.path.join(TEMP_PATH)


def rename_columns(df):
    df.rename(
        columns = {
            "PassengerId" : "id",
            "HomePlanet" : "home_planet",
            "CryoSleep" : "cryo_sleep",
            "Cabin" : "cabin",
            "Destination" : "destination",
            "Age" : "age",
            "VIP" : "vip",
            "RoomService" : "room_service",
            "FoodCourt" : "food_court",
            "ShoppingMall" : "shopping_mall",
            "Spa" : "spa",
            "VRDeck" : "vr_deck",
            "Name" : "name",
            "Transported" : "transported"
       },
        inplace = True
    )


def fill_values_by_based_on_group(df,column_name):
    """
    Fills values by based on passenger id grouping
    :param df: dataframe
    :param column_name: column name
    :return: dataframe with filled values
    """
    
    all_unqiue_values_of_column = list(df[column_name].unique())
    all_unqiue_values_of_column = [each_value for each_value in all_unqiue_values_of_column if not isinstance(each_value,type(np.nan))]
    print("Null Values before: ",df[column_name].isnull().sum())
    print("all unqiue Values: ",all_unqiue_values_of_column)
    
    for index, row in df.iterrows():
        if row[column_name] not in all_unqiue_values_of_column:
            lookup_group = row["id"].split("_")[0]
            found_group = df[df["id"].str.contains(lookup_group)][column_name]
            
            output = [each_value for each_value in found_group if each_value in all_unqiue_values_of_column]
            output = list(set(output))
            
            if len(output)>=1:
                df[column_name].iloc[index] = output[0]

    print("Null Values after: ",df[column_name].isnull().sum())
    return df


def fill_values_by_based_on_mean_and_variance(df, column_name):
    """
    Fills values by based on mean and variance
    :param df: dataframe
    :param column_name: column name
    :return: dataframe with filled values
    """
    value_count_list = dict(df[column_name].value_counts())
    total_rows = len(df[column_name])
    total_nan = int(df[column_name].isnull().sum())
    print("Total stats: {0}, {1}, {2}".format(value_count_list,total_nan,total_rows))
    

if __name__ == '__main__':
    train_df = pd.read_csv(data_csv_path)
    test_df = pd.read_csv(test_csv_path)
    
    # renaming columns
    rename_columns(train_df)
    rename_columns(test_df)
    
    # fill_values_by_based_on_group
    train_df = fill_values_by_based_on_group(train_df,"home_planet")
    test_df = fill_values_by_based_on_group(test_df,"home_planet")

    # fill_values_by_based_on_mean_and_variance
    train_df = fill_values_by_based_on_mean_and_variance(train_df,"home_planet")
    


