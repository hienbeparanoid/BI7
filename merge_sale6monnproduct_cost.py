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

#calculate cost
merged_df['cost']=merged_df['quantity_sold']*merged_df['current_cost']

# Nhóm dữ liệu theo cột 'Month' và tính tổng chi phí sản phẩm
cost_by_month = merged_df.groupby('Month')['cost'].sum()


#vì index là các tháng không theo thứ tự ta mong muốn nên ta tạo lại index và value
data = {'Month': ['11', '12', '1', '2', '3', '4'],
        'Cost': [47837.3115, 45443.9010, 38082.0795, 33593.8145, 38764.3310, 60343.3875]}
df = pd.DataFrame(data)

#plot the graph
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,6))
plt.bar(df['Month'],df['Cost'], label='Cost',color='#F09B59')
plt.xlabel('Month', fontsize=10, fontweight='bold')
plt.ylabel('Cost', fontsize=10, fontweight='bold')
plt.title('Cost by month', fontsize=16, fontweight='bold')

#show the value of each bar
for i, value in enumerate(df['Cost']):
    plt.text(i, value, str(value), ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.show()

