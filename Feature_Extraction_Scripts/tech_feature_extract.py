from finta import TA
import pandas as pd
import os




""" 
Performs technical feature extraction using a provided function, and stores
the resulting technical features in dataframes

Args:
    technical_function:     The function with which to extract the features
                            (E.g., TA.EMA)
    dataframe_dict          Dictionary containing the all the dataframes to
                            individually extract features from. The keys in 
                            the dictionary should be the names of the 
                            dataframes
    path_to_feature_dir     Path to the directory within which to store the
                            extracted features as .csv files
    function_name           Name of processing method
"""
def extract_technical_features(technical_function, dataframe_dict, 
                               path_to_feature_dir, function_name):
    # Make the parent directory if it does not yet exist
    if (os.path.exists(path_to_feature_dir) is False):
        os.mkdir(path_to_feature_dir)
        exchange_rate_dfs[filename] = exchange_rate_df
    # Extract the date column from the dataframes
    df_name = list(dataframe_dict.keys())[0]
    date_column = dataframe_dict[df_name][["Date"]]

    # Perform the feature processing on each of the dataframes and 
    # write the result to their own .csv files
    for df_name in dataframe_dict:
        individual_df = dataframe_dict[df_name]
        ema_df = pd.DataFrame(technical_function(individual_df))
        ema_df.insert(loc=0, column="Date", value=date_column)
        # Write the CSV fo file
        path_to_file = path_to_feature_dir + df_name + "_" + function_name +".csv"
        if os.path.exists(path_to_file) is False:
            ema_df.to_csv(path_to_file, sep=",", index=False)



if __name__ == "__main__":
    # Make directory to store the processed features in if it doesn't already exist
    cwd = os.getcwd()
    processed_feat_dir = cwd + "/../Processed_Features"
    if os.path.exists(processed_feat_dir) is False:
        os.mkdir(processed_feat_dir)

    # Read in the dataframes
    exchange_rate_dfs = {}

    path_to_datasets = "../Datasets/"

    
    dataset_filenames = ["EUR-GBP", "GBP-CHF", "USD-CHF", "USD-EUR", "USD-GBP"]
    for filename in dataset_filenames:
        exchange_rate_df = pd.read_csv(path_to_datasets + filename
                                                  +".csv", parse_dates=True)
        # Make the open, close, high, and low column names lowercase to match
        # formatting requiremetns of TA modulue
        exchange_rate_df.rename(columns={'Open':'open', 'High':'high', 
                                         'Low':'low', 'Close':'close'}, inplace=True)
        exchange_rate_dfs[filename] = exchange_rate_df

    date_column = exchange_rate_df[["Date"]]
    ### Extract Technical Features
    path_to_processed_feats = cwd + "/../Processed_Features/"
    # Calculate the Exponential Moving Averages for each exchange rate and store
    # them in a csv file
    path_to_EMA_dir = path_to_processed_feats + "Exp_Moving_Avg/"
    extract_technical_features(TA.EMA, exchange_rate_dfs, path_to_EMA_dir,
                               "EMA")
    
    # Calculate the Percentage Price Oscillator for each exchange rate
    path_to_PPO_dir = path_to_processed_feats + "Percent_Price_Osc/"
    extract_technical_features(TA.PPO, exchange_rate_dfs, path_to_PPO_dir,
                               "PPO")
    
    # Calculate the Percentage Price Oscillator for each exchange rate
    path_to_MACD_dir = path_to_processed_feats + "Mov_Avg_Converg_Diverg/"
    extract_technical_features(TA.MACD, exchange_rate_dfs, path_to_MACD_dir,
                               "MACD")
    
    # Calculate the Bollinger Bands for each exchange rate
    path_to_BBANDS_dir = path_to_processed_feats + "Bollinger_Bands/"
    extract_technical_features(TA.BBANDS, exchange_rate_dfs, path_to_BBANDS_dir,
                               "BBANDS")
    
    # Calculate the True Range for each exchange rate
    path_to_TR_dir = path_to_processed_feats + "True_Range/"
    extract_technical_features(TA.TR, exchange_rate_dfs, path_to_TR_dir,
                               "TR")
    
    # Calculate the True Range for each exchange rate
    path_to_ATR_dir = path_to_processed_feats + "Avg_True_Range/"
    extract_technical_features(TA.ATR, exchange_rate_dfs, path_to_ATR_dir,
                               "ATR")




