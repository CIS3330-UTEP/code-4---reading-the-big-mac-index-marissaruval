import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
filename ="./big-mac-full-index.csv"
df = pd.read_csv(filename)

def get_big_mac_price_by_year(year,country_code):
    query_str = f"(iso_a3 == '{country_code.upper()}' and date.str.contains('{year}'))"
    arg_df = df.query(query_str)
    return round(arg_df['dollar_price'].mean(),2)
    

def get_big_mac_price_by_country(country_code):
    query_str = f"(iso_a3 == '{country_code.upper()}')"
    arg_df = df.query(query_str)
    return round(arg_df['dollar_price'].mean(),2)
    

def get_the_cheapest_big_mac_price_by_year(year):
    query_str = f"(date.str.contains('{year}'))"
    arg_df = df.query(query_str)
    min_df_idx =  arg_df['dollar_price'].idxmin()
    min_item = arg_df.loc[min_df_idx]
    return f"{min_item['name']}({min_item['iso_a3']}): ${round(min_item['dollar_price'],1)}"
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    query_str = f"(date.str.contains('{year}'))"
    arg_df = df.query(query_str)
    max_df_idx =  arg_df['dollar_price'].idxmax()
    max_item = arg_df.loc[max_df_idx]
    return f"{max_item['name']}({max_item['iso_a3']}): ${round(max_item['dollar_price'],1)}"
    pass # Remove this line and code your function

if __name__ == "__main__":
    x = get_big_mac_price_by_year(2003, "arg")
    print(x)
    x = get_big_mac_price_by_country ("arg")
    print(x)
    x = get_the_cheapest_big_mac_price_by_year (2008)
    print(x)
    x = get_the_most_expensive_big_mac_price_by_year (2003)
    print(x)
    pass # Remove this line and code your user interface