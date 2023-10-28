def calculate_slopes(time_series, window_size=3, overlap_size=0):
    """
    Calculate slopes of windows in time series data.

    Parameters:
    - time_series: NumPy array containing the time series data.
    - window_size: Size of the window for calculating slopes.
    - overlap_size: Size of the overlap between consecutive windows.

    Returns:
    - slopes: NumPy array containing the slopes of each window.
    """
    num_samples = len(time_series)
    num_windows = num_samples // window_size

    slopes = np.empty(num_windows)

    for i in range(num_windows):

        start = i * window_size
        end = start + window_size

        window_data = time_series[start:end]
        delta_y = window_data[-1] - window_data[0]
        slope = delta_y / window_size
        slopes[i] = slope

    return slopes