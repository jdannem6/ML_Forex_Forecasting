Directory Structure:
- USDCHF=X
- USDGBP=X
- USDCHF=X
- EURGBP=X
- GBPCHF=X
- USDCHF=X.cvs
- USDGBP=X.cvs
- USDCHF=X.cvs
- EURGBP=X.cvs
- GBPCHF=X.cvs
- tech_analysis.py

# tech_analysis.py
Will read through all cvs files (e.g., USDCHF=X.cvs) under current folders and save technical features as cvs files (e.g. USDCHF=X_CMO9.csv) under corresponding subfolders (e.g. USDCHF=X)

# Dataset
1. USD/EUR:
https://finance.yahoo.com/quote/USDEUR%3DX/history?p=USDEUR%253DX
1. USD/GBP:
https://finance.yahoo.com/quote/USDGBP%3DX/history?p=USDGBP%253DX
1. USD/CHF:
https://finance.yahoo.com/quote/USDCHF%3DX/history?p=USDCHF%253DX
1. EUR/GBP:
https://finance.yahoo.com/quote/EURGBP%3DX/history?p=EURGBP%253DX
1. GBP/CHF:
https://finance.yahoo.com/quote/GBPCHF%3DX/history?p=GBPCHF%253DX