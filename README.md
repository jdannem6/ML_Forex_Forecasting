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

## How to run VARIMA models
- All of the VARIMA models are Jupyter notebooks named "VARIMA_[currency_rate].ipynb. For example, the VARIMA model for predicting the USD/EUR rate is VARIMA_usd_eur.ipynb. Run any of these notebooks to test the models

## How to test older models
- The older models, such as the support vector regression, ridge regression, ARIMA models, etc. are all stored in the old folder.

### Acknowledgements
The VARIMA scripts make use of code from [1] for implementing the Augmented Dickey Fuller (ADF) and the Grangers Causality Test. These code snippets were solely used to determine necessary attributes of underlying data before training the models
[1] Prabhakaran, S. (2022, August 30). Vector autoregression (VAR) - comprehensive guide with examples in Python. Machine Learning Plus. https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/ 
