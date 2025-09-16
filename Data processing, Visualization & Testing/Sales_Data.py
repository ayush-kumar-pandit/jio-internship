import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('appliance_sales.csv')

# Create a figure and 3 subplots arranged horizontally
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1: Line plots for product sales over quarters
axs[0].plot(data['Quarter'], data['Fridge'], label='Fridge')
axs[0].plot(data['Quarter'], data['Dishwasher'], label='Dishwasher')
axs[0].plot(data['Quarter'], data['Washing Machine'], label='Washing Machine')
axs[0].set_title('Product Sales Over Quarters')
axs[0].set_xlabel('Quarters')
axs[0].set_ylabel('Sales in Million $')
axs[0].legend()
axs[0].tick_params(axis='x', rotation=45)

# Plot 2: Pie chart for total sales distribution
sales = data[['Fridge', 'Dishwasher', 'Washing Machine']].sum()
axs[1].pie(sales, labels=sales.index, autopct='%1.1f%%', shadow=True, startangle=140)
axs[1].set_title('Sales Distribution by Product')

# Plot 3: Bar plot for sales data by quarter
data.plot(kind='bar', x='Quarter', ax=axs[2])
axs[2].set_title('Sales by Quarter')
axs[2].set_xlabel('Quarter')
axs[2].set_ylabel('Sales in Million $')
axs[2].tick_params(axis='x', rotation=45)

# Adjust layout for neatness
plt.tight_layout()

# Show combined dashboard
plt.show()
