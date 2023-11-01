import glob
import os
import pandas as pd
from finta import TA


csv_files = glob.glob('*.csv')


for csv_filename in csv_files:
    df = pd.read_csv(csv_filename, index_col="Date", parse_dates=True)
    df.columns = ["open", "high", "low", "close", "adj close", "volume"]
    df['open'] = df['open'].astype(float)
    df['high'] = df['high'].astype(float)
    df['low'] = df['low'].astype(float)
    df['close'] = df['close'].astype(float)
    df['adj close'] = df['adj close'].astype(float)
    df['volume'] = df['volume'].astype(float)

    saved_dir = csv_filename[:-4]

    # """"ROC"""
    # # ROC1
    # period = 1
    # processed_file_name = os.path.splitext(csv_filename)[0] + f"_ROC{period}.csv"
    # TA.ROC(df, period).to_csv(os.path.join(saved_dir, processed_file_name), index=True)
    # print(f"Processed and saved {csv_filename} as {processed_file_name}")

    # # ROC5
    # period = 5
    # processed_file_name = os.path.splitext(csv_filename)[0] + f"_ROC{period}.csv"
    # TA.ROC(df, period).to_csv(os.path.join(saved_dir, processed_file_name), index=True)
    # print(f"Processed and saved {csv_filename} as {processed_file_name}")

    # # ROC20
    # period = 20
    # processed_file_name = os.path.splitext(csv_filename)[0] + f"_ROC{period}.csv"
    # TA.ROC(df, period).to_csv(os.path.join(saved_dir, processed_file_name), index=True)
    # print(f"Processed and saved {csv_filename} as {processed_file_name}")

    # """"Williams %R"""
    # # WILLIAMS
    # period = 14 # default
    # processed_file_name = os.path.splitext(csv_filename)[0] + f"_WILLIAMS{period}.csv"
    # TA.WILLIAMS(df, period).to_csv(os.path.join(saved_dir, processed_file_name), index=True)
    # print(f"Processed and saved {csv_filename} as {processed_file_name}")

    # """"Relative Strenght Index 'RSI'"""
    # # RSI
    # period = 14 # default
    # processed_file_name = os.path.splitext(csv_filename)[0] + f"_RSI{period}.csv"
    # TA.RSI(df, period).to_csv(os.path.join(saved_dir, processed_file_name), index=True)
    # print(f"Processed and saved {csv_filename} as {processed_file_name}")

    # """"Chande Momentum Oscillator 'CMO'"""
    # # CMO
    # period = 9 # default
    # processed_file_name = os.path.splitext(csv_filename)[0] + f"_CMO{period}.csv"
    # TA.CMO(df, period).to_csv(os.path.join(saved_dir, processed_file_name), index=True)
    # print(f"Processed and saved {csv_filename} as {processed_file_name}")

    # """"Double Exponential Moving Average 'DEMA'"""
    # # DEMA
    # period = 9 # default
    # processed_file_name = os.path.splitext(csv_filename)[0] + f"_DEMA{period}.csv"
    # TA.DEMA(df, period).to_csv(os.path.join(saved_dir, processed_file_name), index=True)
    # print(f"Processed and saved {csv_filename} as {processed_file_name}")

    # """"Triple Exponential Moving Average 'TEMA'"""
    # # TEMA
    # period = 9 # default
    # processed_file_name = os.path.splitext(csv_filename)[0] + f"_TEMA{period}.csv"
    # TA.TEMA(df, period).to_csv(os.path.join(saved_dir, processed_file_name), index=True)
    # print(f"Processed and saved {csv_filename} as {processed_file_name}")

    # """"Stochastic Oscillator %K 'STOCH'"""
    # # STOCH
    # period = 14 # default
    # processed_file_name = os.path.splitext(csv_filename)[0] + f"_STOCH{period}.csv"
    # TA.RSI(df, period).to_csv(os.path.join(saved_dir, processed_file_name), index=True)
    # print(f"Processed and saved {csv_filename} as {processed_file_name}")
