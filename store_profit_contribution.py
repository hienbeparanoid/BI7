import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read data from 'Sale_2022'
df_6months = pd.read_csv('./data/Historical_saleslast6months.csv')

#read data from 'Sale_2021' and convert 'transaction_date' to datetime
df_product = pd.read_csv('./data/Dim_product.csv')

#merge data from 'Sale_2021' and 'Sale_2022'
merged_df = pd.merge(df_6months, df_product, on='product_id', how='left')

#create a new column 'Month' from 'transaction_date'
merged_df['Month'] = merged_df['transaction_date'].str.slice(start=0, stop=2,step=1)
merged_df.head()

# Loại bỏ ký tự '/' từ cột 'month'
merged_df['Month'] = merged_df['Month'].str.replace('/', '')

#calculate sales
merged_df['Doanh thu']=merged_df['quantity_sold']*merged_df['unit_price']
merged_df.head()


#calculate cost
merged_df['cost']=merged_df['quantity_sold']*merged_df['current_cost']


# Nhóm dữ liệu theo cột 'Cửa hàng' và tính tổng doanh thu cho mỗi cửa hàng
revenue_by_store = merged_df.groupby('store_id')['Doanh thu'].sum()

# Nhóm dữ liệu theo cột 'Cửa hàng' và tính tổng doanh thu và chi phí cho mỗi cửa hàng
revenue_by_store = merged_df.groupby('store_id')['Doanh thu'].sum()
cost_by_store = merged_df.groupby('store_id')['cost'].sum()

# Tính lợi nhuận của mỗi cửa hàng bằng cách trừ chi phí từ doanh thu
profit_by_store = revenue_by_store - cost_by_store

# Tính tổng lợi nhuận của tất cả các cửa hàng
total_profit = profit_by_store.sum()

# Tính tỉ lệ phần trăm đóng góp lợi nhuận của mỗi cửa hàng
contribution_percent = (profit_by_store / total_profit) * 100

# Tạo biểu đồ pie chart
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(contribution_percent, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12}, colors =['#F09B59', '#85D3D4', '#FEDD9E'])

legend_labels = profit_by_store.index
ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5),labels=legend_labels, fontsize=12)


plt.title('Profit contribution by store', fontsize=16, fontweight='bold')

plt.show()