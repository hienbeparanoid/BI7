import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots(figsize=(8, 4))

customers = pd.read_csv('./data/Dim_customer.csv')

customers['birthdate'] = pd.to_datetime(customers['birthdate'])

#calculate the number of customer by birthday
customer_by_birthday = customers['birthdate'].dt.year.value_counts().sort_index()

#draw a line chart
plt.plot(customer_by_birthday.index, customer_by_birthday.values, marker='o', label='Birthday')

#label each axis
plt.xlabel('Year', fontsize=10, fontweight='bold')
plt.ylabel('Amount', fontsize=10, fontweight='bold')
plt.title('The quantity of Customers by Birthday', fontsize=16, fontweight='bold')

plt.legend()
plt.show()