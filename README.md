# Dataset
1. USD/EUR:
https://finance.yahoo.com/quote/USDEUR%3DX/history?p=USDEUR%253DX
2. USD/GBP:
https://finance.yahoo.com/quote/USDGBP%3DX/history?p=USDGBP%253DX
3. USD/CHF:
https://finance.yahoo.com/quote/USDCHF%3DX/history?p=USDCHF%253DX
4. EUR/GBP:
https://finance.yahoo.com/quote/EURGBP%3DX/history?p=EURGBP%253DX
5. GBP/CHF:
https://finance.yahoo.com/quote/GBPCHF%3DX/history?p=GBPCHF%253DX
6. EUR/CHF:
https://finance.yahoo.com/quote/EURCHF%3DX/history?p=EURCHF%3DX

# How to run svr.ipynb
- Set feat_dir as the path to which csv files and generate_features.py is stored
- 'Run all' for each notebook. Latest 5d predictions are stored in predictions_T_svr.csv, with each row as a 5-day prediction and rows generated in the order of notebooks run
- Run 'predictions_T.ipynb' to transpose the matrix in 'predictions_T_svr.csv' (from 6*5 to 5*6)