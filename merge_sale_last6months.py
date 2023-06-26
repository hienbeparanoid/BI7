import pandas as pd

#read data from 'Sale_2022'
df_2022 = pd.read_csv('./data/Historical_sales2022.csv')

#read data from 'Sale_2021' and convert 'transaction_date' to datetime
df_2021 = pd.read_csv('./data/Historical_sales2021.csv')
df_2021['transaction_date'] = pd.to_datetime(df_2021['transaction_date'])

#filter data of month 11 and 12 from 'Sale_2021'
df_2021_nov_dec = df_2021[(df_2021['transaction_date'].dt.month == 11) | (df_2021['transaction_date'].dt.month == 12)]

#merge data from 'Sale_2021' and 'Sale_2022'
merged_df = pd.concat([df_2021_nov_dec, df_2022])

#save the merged data to csv
merged_df.to_csv('Historical_saleslast6months.csv', index=False)
