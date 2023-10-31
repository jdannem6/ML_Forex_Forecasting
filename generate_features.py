from sp_sine_fourier_feature_extraction import sp_feature_extraction
import stats_feats
from slope_feature_extraction import calculate_slopes
import utils_ta
import pandas as pd

def generate_features(df):
    '''
    This function generates all the features needed for ML FOREX forecasting.

    Inputs:
     - df: The raw currency exchange rate DataFrame (The dates should be from the current day - (year + month) to the current day)

    Outputs:
     - df_feats: A DataFrame containing the features
    '''


    # Extract the signal processing features (sine and Fourier series parameters)
    df_spfeats = sp_feature_extraction(df)
    
    # Extract the slopes
    df_slopes = calculate_slopes(df)

    # Merge the SP features and the slope features
    df_feats = df_spfeats.merge(df_slopes, how='inner', on='Date')

    # Extract the statistical features
    df_stat_feats = [stats_feats.extract_autocorr(df), stats_feats.extract_pca(df), 
                    stats_feats.extract_ica(df), stats_feats.extract_mean_abs_change(df)]
    
    # Merge the statistical features
    for i in range(4):
        df_feats = df_feats.merge(df_stat_feats[i], how='inner', on='Date')

    # Extract the technical features
    df_ta_feats = pd.DataFrame({'Date': df['Date'], 'ROC1': utils_ta.ROC1(df), 'ROC5': utils_ta.ROC5(df),
                                'ROC20': utils_ta.ROC20(df), 'WILLIAMS14': utils_ta.WILLIAMS14(df),
                                'RSI14': utils_ta.RSI14(df), 'CMO9': utils_ta.CMO9(df),
                                'DEMA9': utils_ta.DEMA9(df), 'TEMA9': utils_ta.TEMA9(df),
                                'STOCH14': utils_ta.STOCH14(df)})
    
    # Merge the technical features
    df_feats = df_feats.merge(df_ta_feats, how='inner',on='Date')

    # Re-arrange the columns
    cols = list(df_feats.columns)
    df_feats = df_feats[[cols[cols.index('Date')]] + [x for x in cols if x != 'Date' and x != 'Close'] + [cols[cols.index('Close')]]]

    return df_feats