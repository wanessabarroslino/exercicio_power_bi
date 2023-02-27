import pandas as pd
df = pd.read_csv('disney_movies.csv')

df['release_date'] = pd.to_datetime(df['release_date'])
df['total_gross'] = pd.to_numeric(df['total_gross'])
df['inflation_adjusted_gross'] = pd.to_numeric(df['inflation_adjusted_gross'])

print(df)