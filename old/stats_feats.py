import numpy as np
import pandas as pd


# Main feature extraction functions
# All functions return features with same length as input dataframe
# except extract_mean_abs_change which needs win_size dates f=before the starting date to extract features

def extract_autocorr(df):

    column = df['Close']
    feats = []
    autocorr = pd.DataFrame(df['Date'])
    for lag in range(1, len(column) + 1):
        feats.append(autocorrelation(column, lag))
    
    autocorr['autocorrelation'] = feats

    return autocorr

def extract_pca(df):

    column = df['Close'].values
    column -= np.mean(column)

    u, _, _ = np.linalg.svd(np.outer(column, column))

    pca = pd.DataFrame(df['Date'])
    pca['pca'] = u[:, 0]

    return pca

def extract_ica(df):

    column = df['Close'].values.reshape(1, -1)

    ica = pd.DataFrame(df['Date'])
    ica['ica'] = ICA(column).T

    return ica

def extract_mean_abs_change(df, win_size = 30):

    # this function gives features for (a + win_size, b) dates if the data has dates from (a, b)
    # hence use win_size dates before the starting date to extract features

    column = df['Close'].values
    feats = []
    for t in range(len(column)):
        if t - win_size < 0:
            feats.append(0)
        else:
            feats.append(mean_abs_change(column[t - win_size: t]))

    mean_abs = pd.DataFrame(df['Date'])
    mean_abs['mean_abs'] = feats

    return mean_abs



# Helper functions
# NOT to be used directly for feature extraction

def autocorrelation(x, lag):
    """
    Calculates the autocorrelation of the specified lag, according to the formula [1]

    .. math::

        \\frac{1}{(n-l)\\sigma^{2}} \\sum_{t=1}^{n-l}(X_{t}-\\mu )(X_{t+l}-\\mu)

    where :math:`n` is the length of the time series :math:`X_i`, :math:`\\sigma^2` its variance and :math:`\\mu` its
    mean. `l` denotes the lag.

    .. rubric:: References

    [1] https://en.wikipedia.org/wiki/Autocorrelation#Estimation

    :param x: the time series to calculate the feature of
    :type x: numpy.ndarray
    :param lag: the lag
    :type lag: int
    :return: the value of this feature
    :return type: float
    """
    # This is important: If a series is passed, the product below is calculated
    # based on the index, which corresponds to squaring the series.
    if isinstance(x, pd.Series):
        x = x.values
    if len(x) < lag:
        return np.nan
    # Slice the relevant subseries based on the lag
    y1 = x[: (len(x) - lag)]
    y2 = x[lag:]
    # Subtract the mean of the whole series x
    x_mean = np.mean(x)
    # The result is sometimes referred to as "covariation"
    sum_product = np.sum((y1 - x_mean) * (y2 - x_mean))
    # Return the normalized unbiased covariance
    v = np.var(x)
    if np.isclose(v, 0):
        return np.NaN
    else:
        return sum_product / ((len(x)) * v)

def ICA(M):

    mu = np.mean(M, axis = 1, keepdims=True)
    M = M - mu

    Corr = M @ M.T / M.shape[0]

    U_ica, S, Vh = np.linalg.svd(Corr.T)

    eig_vals = np.diag(S ** (-0.5))

    C = eig_vals @ U_ica.T

    X_hat = C @ M

    D = np.zeros_like(X_hat @ X_hat.T)

    for x in X_hat.T:
        D += np.linalg.norm(x) ** 2 * np.outer(x, x)

    B, _, _ = np.linalg.svd(D)

    A = B.T @ C
    H = A @ M

    return H

def mean_abs_change(x):
    return np.mean(np.abs(np.diff(x)))
