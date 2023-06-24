import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

customers = pd.read_csv('./data/Dim_customer.csv')

#count the number of each gender type
gender_count = customers['gender'].value_counts()
male_count = gender_count.get('M',0)
female_count = gender_count.get('F',0)

#draw a bar chart
plt.figure(figsize=(6,6))
plt.bar(['M','F'], [male_count,female_count], color=['blue','purple'])

#label each axis
plt.xlabel('Gioi tinh')
plt.ylabel('So luong')
plt.title('So luong khach hang theo gioi tinh')

plt.show()

