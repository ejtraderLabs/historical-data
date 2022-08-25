# forex historical csv data
Each symbol contains m15, m30, h1, h4, d1 data and the data length is 10 years.

# Example
When reading csv files in python, the URL must be "raw.githubusercontent.com".
```python
import pandas as pd

def get_forex_data(symbol: str, timeframe: str):
    """
    :param symbol: AUDJPY, AUDUSD, EURCHF, EURGBP, EURJPY, EURUSD, GBPJPY, GBPUSD, USDCAD, USDCHF, USDJPY, XAUUSD
    :param timeframe: m15, m30, h1, h4, d1
    :return: pandas DataFrame
    """
    symbol = symbol.upper()

    url = "https://raw.githubusercontent.com//ejtraderLabs/historical-data/main/"
    url += symbol + "/" + symbol + timeframe.lower() + ".csv"

    return pd.read_csv(url)



df = data.get_forex_data("EURUSD", "h1")

print(df.head())
```
```
                  Date      open      high       low     close  tick_volume
0  2012-11-16 00:00:00  127801.0  127835.0  127777.0  127810.0          869
1  2012-11-16 01:00:00  127809.0  127837.0  127686.0  127736.0         1408
2  2012-11-16 02:00:00  127738.0  127769.0  127706.0  127734.0         1285
3  2012-11-16 03:00:00  127738.0  127762.0  127673.0  127695.0         1210
4  2012-11-16 04:00:00  127694.0  127771.0  127641.0  127724.0         1487
```
