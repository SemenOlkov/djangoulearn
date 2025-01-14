import pandas as pd


df = pd.read_csv('currency.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m')
mask = df['date'] >= pd.to_datetime('2016-07', format='%Y-%m')
df.loc[mask, 'BYR'] = df.loc[mask, 'BYN']
df = df.drop(columns=['BYN'])
df['date'] = df['date'].apply(lambda x: x.isoformat()[0:7])
df.to_csv('corrected_currency.csv', index=False)
