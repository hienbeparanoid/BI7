import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,6))

data = pd.read_csv('./data/Dim_customer.csv')

#calculate the age of each customer
current_year = datetime.now().year
data['birthdate'] = pd.to_datetime(data['birthdate'])
data['age'] = current_year - data['birthdate'].dt.year

# Group the customer data by store and age, and calculate the number of customers per store and age
store_age_counts = data.groupby(['store_id', 'age']).size().reset_index(name='amount')

# Get a list of unique store IDs
store_ids = store_age_counts['store_id'].unique()

for store_id in store_ids:
    store_data = store_age_counts[store_age_counts['store_id'] == store_id]
    plt.plot(store_data['age'], store_data['amount'], label=f"Store {store_id}")

# Set x and y axis labels
plt.xlabel('Age', fontsize=10, fontweight='bold')
plt.ylabel('Amount', fontsize=10, fontweight='bold')

# Set title for the graph
plt.title('Number of Customers by Age and Store', fontsize=16, fontweight='bold')

plt.legend()
plt.show()