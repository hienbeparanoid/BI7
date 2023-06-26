import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read data from 'historical_saleslast6months.csv'
df = pd.read_csv('./data/Historical_saleslast6months.csv')

#create a new column 'Month' from 'transaction_date'
df['Month'] = df['transaction_date'].str.slice(start=0, stop=2,step=1)
df.head()

# Loại bỏ ký tự '/' từ cột 'month'
df['Month'] = df['Month'].str.replace('/', '')


#calculate sales
df['Doanh thu']=df['quantity_sold']*df['unit_price']
df.head()

moving_column = df.pop('Doanh thu')
df.insert(9, 'Doanh thu', moving_column)
df.head()


# Nhóm dữ liệu theo cột 'Cửa hàng' và tính tổng doanh thu cho mỗi cửa hàng
revenue_by_store = df.groupby('store_id')['Doanh thu'].sum()
print(revenue_by_store)
# Tính tổng doanh thu của tất cả các cửa hàng
total_revenue = revenue_by_store.sum()

# Tính tỉ lệ phần trăm đóng góp doanh thu của mỗi cửa hàng
contribution_percent = (revenue_by_store / total_revenue) * 100

# Tạo biểu đồ pie chart
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(contribution_percent, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12}, colors =['#F09B59', '#85D3D4', '#FEDD9E'])


legend_labels = revenue_by_store.index
ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5),labels=legend_labels, fontsize=12)

plt.title('Sales contribution by store', fontsize=16, fontweight='bold')

plt.show()