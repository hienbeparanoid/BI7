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

salebymonth = merged_df.groupby(['Month']).sum()['Doanh thu']

#calculate cost
merged_df['cost']=merged_df['quantity_sold']*merged_df['current_cost']

# Nhóm dữ liệu theo cột 'Month' và tính tổng chi phí sản phẩm
cost_by_month = merged_df.groupby('Month')['cost'].sum()

#calcualte profit
profit = salebymonth - cost_by_month
marginprofit = profit/salebymonth*100
print(marginprofit)
#vì index là các tháng không theo thứ tự ta mong muốn nên ta tạo lại index và value
data = {'Month': ['11', '12', '1', '2', '3', '4'],
        'marginProfit': [74.058041, 74.046092, 74.069765, 74.053551, 74.053666, 74.028742]}
df = pd.DataFrame(data)

#plot the graph
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,6))
plt.bar(df['Month'],df['marginProfit'], label='Cost',color='#F09B59')
plt.xlabel('Month', fontsize=10, fontweight='bold')
plt.ylabel('MarginProfit', fontsize=10, fontweight='bold')
plt.title('MarginProfit by month', fontsize=16, fontweight='bold')

#show the value of each bar
for i, value in enumerate(df['marginProfit']):
    plt.text(i, value, str(value), ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.show()