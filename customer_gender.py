import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

customers = pd.read_csv('./data/Dim_customer.csv')

#count the number of each gender type
gender_count = customers['gender'].value_counts()
male_count = gender_count.get('M',0)
female_count = gender_count.get('F',0)
notspecified_count = gender_count.get('Not Specified',0)

Gender = ['M','F','Not Specified']
Count = [male_count,female_count,notspecified_count]

#draw a bar chart
plt.figure(figsize=(6,6))
plt.bar(Gender, Count, color=['#F09B59','#1783DB','#BC9DC7'])

#label each axis
plt.xlabel('Giới tính', fontsize=10, fontweight='bold')
plt.ylabel('Số lượng', fontsize=10, fontweight='bold')
plt.title('Số lượng khách hàng theo giới tính', fontsize=16, fontweight='bold')

#show the value of each bar
for i, value in enumerate(Count):
    plt.text(i, value, str(value), ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.show()

