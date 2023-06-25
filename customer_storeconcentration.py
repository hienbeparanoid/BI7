import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8,10))

data1 = pd.read_csv('./data/Dim_customer.csv')
data2 = pd.read_csv('./data/Dim_store.csv')

store_counts = data1['store_id'].value_counts().reset_index()
store_counts.columns = ['store_id', 'customer_count']

# Kết hợp dữ liệu từ hai DataFrame dựa trên cột 'store_id'
combined_data = pd.merge(data2, store_counts, on='store_id', how='left')

# Calculate the scaling factor based on the maximum customer count
scaling_factor = 1000 / combined_data['customer_count'].max()

# Calculate the scaled dot size for each store
combined_data['dot_size'] = combined_data['customer_count'] * scaling_factor

#Scatter Plot
plt.scatter(combined_data['store_longitude'], combined_data['store_latitude'], s=combined_data['dot_size'], c= 'red', alpha=0.5)

# Label the stores
for i, row in combined_data.iterrows():
    plt.annotate(row['store_id'], (row['store_longitude'], row['store_latitude']), fontsize=8, ha='center', va='center')
    
# Label the stores with customer counts
for x, y, count in zip(combined_data['store_longitude'], combined_data['store_latitude'], combined_data['customer_count']):
    plt.text(x+0.0095, y, f"{count} customers", fontsize=8, ha='center', va='bottom')

# plt.axis('equal')
plt.xlabel('Longtitude', fontsize=10, fontweight='bold')
plt.ylabel('Latitude', fontsize=10, fontweight='bold')
plt.title('Store Concentration by Location', fontsize=16, fontweight='bold')

plt.show()
