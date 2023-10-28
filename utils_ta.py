from finta import TA

def ROC1(df):
    period = 1
    return TA.ROC(df, period)

def ROC5(df):
    period = 5
    return TA.ROC(df, period)

def ROC20(df):
    period = 20
    return TA.ROC(df, period)

def WILLIAMS14(df):
    period = 14 # default
    TA.WILLIAMS(df, period)

def RSI14(df):
    period = 14 # default
    return TA.RSI(df, period)

def CMO9(df):
    period = 9 # default
    TA.CMO(df, period)

def DEMA9(df):
    period = 9 # default
    return TA.DEMA(df, period)

def TEMA9(df):
    period = 9 # default
    return TA.TEMA(df, period)

def STOCH14(df):
    period = 14 # default
    return TA.RSI(df, period)