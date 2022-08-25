import pandas as pd

url = "https://raw.githubusercontent.com/komo135/forex-historical-data/main/EURUSD/EURUSDh1.csv"
df = pd.read_csv(url)

print(df.head())

