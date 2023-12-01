import numpy as np
import pandas as pd

def calculate_slopes(df, window_size=3, overlap_size=0, var='Close'):
    """
    Calculate slopes of windows in time series data.

    Parameters:
    - df: DataFrame containing the time series data.
    - window_size: Size of the window for calculating slopes.
    - overlap_size: Size of the overlap between consecutive windows.

    Returns:
    - slopes_df: DataFrame containing the slopes of each window in one column and their corresponding dates in another column.
    """
    num_samples = df.shape[0]
    slopes = np.zeros((num_samples,))

    for c, index in enumerate(reversed(range(num_samples))):

        start = index - window_size
        if start < 0:
            break
        end = index   

        window_data = df.loc[start:end,var].to_numpy()
        delta_y = window_data[-1] - window_data[0]
        slope = delta_y / window_size
        slopes[c] = slope

    slopes_df = pd.DataFrame({'Date': df.loc[::-1,'Date'], 'Slopes': slopes})

    return slopes_df
