import pandas as pd

filename ="./big-mac-full-index.csv"
df = pd.read_csv(filename)
query_str = "(iso_a3 == 'ARG' and (date.str.startswith('')  ))"
print(query_str)
arg_df = df.query(query_str)
print(round(arg_df['dollar_price'].mean(),2))

min_df_idx =  df['dollar_price'].idxmin()
max_df_idx = df['dollar_price'].idxmax()

print(min_df_idx)
print(max_df_idx)

min_item = df.loc[min_df_idx]
max_item = df.loc[max_df_idx]
print(min_item)
print('/n')
print(max_item)