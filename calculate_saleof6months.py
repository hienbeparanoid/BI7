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

salebymonth = df.groupby(['Month']).sum()['Doanh thu']


#vì index là các tháng không theo thứ tự ta mong muốn nên ta tạo lại index và value
data = {'Month': ['11', '12', '1', '2', '3', '4'],
        'Sale': [184401.31, 175094.64, 146863.61, 129473.65, 149401.96, 232346.80]}
df = pd.DataFrame(data)

#plot the graph
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,6))
plt.bar(df['Month'], df['Sale'], label='Doanh thu',color='#F09B59')
plt.xlabel('Month', fontsize=10, fontweight='bold')
plt.ylabel('Sales', fontsize=10, fontweight='bold')
plt.title('Sales by month', fontsize=16, fontweight='bold')

#show the value of each bar
for i, value in enumerate(df['Sale']):
    plt.text(i, value, str(value), ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.show()
