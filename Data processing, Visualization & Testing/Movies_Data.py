import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('appliance_sales.csv')

plt.figure(figsize = (12,4))

plt.plot(data['Quarter'],data['Fridge'],label = 'Fridge')
plt.plot(data['Quarter'],data['Dishwasher'],label = 'Dishwasher')
plt.plot(data['Quarter'],data['Washing Machine'],label = 'Washing Machine')
plt.title('Product Sales')
plt.ylabel('Sales in Million $')
plt.xlabel('Quarters')
plt.legend()
plt.show()

sales = data[['Fridge','Dishwasher','Washing Machine']].sum()
plt.pie(sales, labels = sales.index, autopct = '%1.1f%%',shadow = True)
plt.show()

data.plot(kind = 'bar', x = 'Quarter')
plt.xticks(rotation = 45)
plt.show()