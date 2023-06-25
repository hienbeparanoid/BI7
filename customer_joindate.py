import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,6))

customers = pd.read_csv('./data/Dim_customer.csv')

customers['customer_since'] = pd.to_datetime(customers['customer_since'])

#calculate the number of customer by customer_since
customer_by_customer_since = customers['customer_since'].dt.year.value_counts().sort_index()

#create a list of years
years = list(set(customer_by_customer_since.index))
years.sort()

#draw a bar chart
plt.bar(years, customer_by_customer_since.reindex(years, fill_value=0), label='Customer Since', color='#E65E89')

#label each axis
plt.xlabel('Year', fontsize=10, fontweight='bold')
plt.ylabel('Amount', fontsize=10, fontweight='bold')
plt.title('The quantity of Customers by Joined day', fontsize=16, fontweight='bold')

#show the value of each bar
for i, value in enumerate(customer_by_customer_since.reindex(years, fill_value=0)):
    plt.text(years[i], value, str(value), ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.legend()
plt.show()