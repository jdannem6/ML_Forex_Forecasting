def find_maximum_profit_path(conversion_rates):

    dp = []
    path = []

    curr = ['USD', 'EUR', 'CHF', 'GBP']
    prev_day = np.array([1, 0, 0, 0])

    for i in range(5):

        USD, EUR, CHF, GBP = prev_day
        USD_EUR, EUR_CHF, EUR_GBP, GBP_CHF, USD_CHF, USD_GBP = conversion_rates[i, :]
        EUR_USD, CHF_EUR, GBP_EUR, CHF_GBP, CHF_USD, GBP_USD = 1/conversion_rates[i, :]

        if i<=3:
            dp = np.array([max(USD*1, EUR*EUR_USD, CHF*CHF_USD, GBP*GBP_USD), max(USD*USD_EUR, EUR*1, CHF*CHF_EUR, GBP*GBP_EUR), max(USD*USD_CHF, EUR*EUR_CHF, CHF*1, GBP*GBP_CHF), max(USD*USD_GBP, EUR*EUR_GBP, CHF*CHF_GBP, GBP*1)])
            path.append(np.array([curr[np.argmax([USD*1, EUR*EUR_USD, CHF*CHF_USD, GBP*GBP_USD])], curr[np.argmax([USD*USD_EUR, EUR*1, CHF*CHF_EUR, GBP*GBP_EUR])], curr[np.argmax([USD*USD_CHF, EUR*EUR_CHF, CHF*1, GBP*GBP_CHF])], curr[np.argmax([USD*USD_GBP, EUR*EUR_GBP, CHF*CHF_GBP, GBP*1])]]))
            prev_day = dp

        elif i==4:
            dp = np.array([USD*1, EUR*EUR_USD, CHF*CHF_USD, GBP*GBP_USD])
            path.append(curr)

    final_path = ['USD']
    index = curr.index(path[-1][np.argmax(dp)])
    print(1000*np.max(dp))

    for i in range(4, -1, -1):
        prev_currency = path[i][index]
        final_path.append(prev_currency)
        index = curr.index(prev_currency)

    final_path.reverse()
    final_path = [final_path[i] + '-' + final_path[i+1] for i in range(5)]

    return final_path