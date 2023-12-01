import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq

def fit_sine_wave(df,var):
    '''
    This function fits a sine wave to a signal.

    Inputs:
     - df: The DataFrame containing the exchange rate data
     - var: Specifies which exchange rate is used (Open, High, Low, Close)

    Outputs:
     - A list containing:
       - opt_offset: The offset of the fitted sine wave
       - opt_amp: The amplitude of the fitted sine wave
       - opt_freq: The frequency of the fitted sine wave
       - opt_phase: The phase of the fitted sine wave
    '''

    # Define the input into the sine wave [0, 4*pi]
    N = df.shape[0]
    t = np.linspace(0, 4*np.pi, N)

    # Initialize the guesses for the offset, amplitude, frequency, and phase of the sine wave
    init_offset, init_amp, init_freq, init_phase = df[var].mean(), 1, 1, 0

    # Define the function to optimize, in this case, we want to minimize the difference
    # between the actual data and our "guessed" parameters
    optimize_func = lambda x: x[0] + x[1]*np.sin(x[2]*t+x[3]) - df[var].to_numpy()
    
    # Find the optimal parameters
    opt_offset, opt_amp, opt_freq, opt_phase = leastsq(optimize_func, [init_offset, init_amp, init_freq, init_phase])[0]
    return [opt_offset, opt_amp, opt_freq, opt_phase]


def fit_fourier_series(df,var):
    '''
    This function fits a Fourier series to a signal.

    Inputs:
     - df: The DataFrame containing the exchange rate data
     - var: Specifies which exchange rate is used (Open, High, Low, Close)

    Outputs:
     - A list containing:
       - opt_offset: The offset of the fitted Fourier series
       - opt_cosamp: The amplitude of the cosine wave component of the fitted Fourier series
       - opt_cosfreq: The frequency of the cosine wave component of the fitted Fourier series
       - opt_cosphase: The phase of the cosine wave component of the fitted Fourier series
       - opt_sinamp: The amplitude of the sine wave component of the fitted Fourier series
       - opt_sinfreq: The frequency of the sine wave component of the fitted Fourier series
       - opt_sinphase: The phase of the sine wave component of the fitted Fourier series
    '''

    # Define the input into the Fourier series [0, 12*pi]
    N = df.shape[0]
    t = np.linspace(0, 12*np.pi, N)
    init_offset, init_cosamp, init_cosfreq, init_cosphase, init_sinamp, init_sinfreq, init_sinphase = df[var].mean(), 1, 1, 0, 1, 1, 0

    # Define the function to optimize, in this case, we want to minimize the difference
    # between the actual data and our "guessed" parameters
    optimize_func = lambda x: x[0] + x[1]*np.cos(x[2]*t+x[3]) + x[4]*np.sin(x[5]*t+x[6]) - df[var].to_numpy()
    opt_offset, opt_cosamp, opt_cosfreq, opt_cosphase, opt_sinamp, opt_sinfreq, opt_sinphase = leastsq(optimize_func, [init_offset, init_cosamp, init_cosfreq, init_cosphase, init_sinamp, init_sinfreq, init_sinphase])[0]
    return [opt_offset, opt_cosamp, opt_cosfreq, opt_cosphase, opt_sinamp, opt_sinfreq, opt_sinphase]

def sp_feature_extraction(df, var='Close', sin_num_days=5, fourier_num_days=30):
    '''
    This function extracts parameters from a fitted sine wave and a fitted Fourier series.

    Inputs:
     - df: The DataFrame containing the exchange rate data
     - var: Specifies which exchange rate is used (Open, High, Low, Close)
     - sin_num_days: The number of days to calculate fitted sine wave features from
     - fourier_num_days: The number of days to calculate fitted Fourier series features from
    
    Outputs:
     - sp_feats: A DataFrame that outputs the fitted sine wave and Fourier Series features
    '''
    # List to store all the feature rows
    features = []
    # Create a copy of the DataFrame and create a new column storing the number of days
    # from the earliest one
    df2 = df.copy()
    df2['t'] = (df2['Date']-df2.loc[0,'Date']).dt.days
    # Loop through each day in reverse and extract features
    for index, row in df2[::-1].iterrows():
        # Do not extract features beyond a year (hard-coded for the dataset sent in
        # where the latest day should be the current date and the earliest day is
        # a year plus a month before the current date)
        if row['t'] < 30:
            break
        
        # Extract exchange rates for the specified number of days for fitting a sine wave (default = 5 days)
        temp = df2.loc[index-sin_num_days:index-1,:]
        # Obtain the fitted sine wave parameters
        opt_sin_params = fit_sine_wave(temp,var)
        # Extract exchange rates for the specified number of days for fitting a Fourier series (default = 30 days)
        temp = df2.loc[index-fourier_num_days:index,:]
        # Obtain the fitted Fourier series parameters
        opt_fourier_params = fit_fourier_series(temp,var)
        # Create a DataFrame row for these features
        entry = [opt_sin_params + opt_fourier_params]
        entry[0].extend([row['t'],row['Date'],row[var]])
        features.append(pd.DataFrame(entry, columns=['opt_sine_offset','opt_sine_amp','opt_sine_freq','opt_sine_phase',
                                        'opt_fourier_offset','opt_fourier_cosamp','opt_fourier_cosfreq',
                                        'opt_fourier_cosphase','opt_fourier_sinamp','opt_fourier_sinfreq',
                                        'opt_fourier_sinphase','t','Date',var]))
        
    # Concatenate all the rows
    sp_feats = pd.concat(features).reset_index(drop=True)
    return sp_feats
