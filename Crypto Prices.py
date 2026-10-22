import requests
import pandas as pd
import numpy as np

response = requests.get("https://api.coingecko.com/api/v3/simple/price",
                        params={"ids": "bitcoin,ethereum,solana", "vs_currencies": "gbp,usd,eur"}, timeout=10,)
if response.status_code == 200:
    data = response.json()
    for name, price in data.items():
        df = pd.DataFrame(list(price.items()), columns=['currency', 'price'])
        df.to_csv(f"{name}.csv", index=False)
else:
    print('Error: ', response.status_code)
#EXTENSION
dataframes = []
for name in ['bitcoin', 'ethereum', 'solana']:
    df = pd.read_csv(f'{name}.csv')
    df['coin'] = name
    dataframes.append(df)

df_combined = pd.concat(dataframes, ignore_index=True)
df_gbp = df_combined[df_combined['currency']=='gbp'].reset_index(drop=True)
highest = df_gbp.loc[df_gbp['price'].idxmax()]
lowest = df_gbp.loc[df_gbp['price'].idxmin()]
avg = df_gbp['price'].mean()
print(f"The highest priced coin in GBP is {highest['coin']} at £{highest['price']:,.2f}")
print(f"The lowest price coin in GBP is {lowest['coin']} at £{lowest['price']:,.2f}")
print(f"The average price in GBP across the three coins is £{avg:,.2f}")