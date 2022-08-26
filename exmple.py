import pandas as pd

def get_forex_data(symbol: str, timeframe: str):
    """
    :param symbol: AUDJPY, AUDUSD, EURCHF, EURGBP, EURJPY, EURUSD, GBPJPY, GBPUSD, USDCAD, USDCHF, USDJPY, XAUUSD
    :param timeframe: m15, m30, h1, h4, d1
    :return: pandas DataFrame
    """
    symbol = symbol.upper()

    url = "https://raw.githubusercontent.com/ejtraderLabs/historical-data/main/"
    url += symbol + "/" + symbol + timeframe.lower() + ".csv"

    return pd.read_csv(url)



df = get_forex_data("EURUSD", "h1")

print(df.head())