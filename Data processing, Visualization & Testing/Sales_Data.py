import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Load data
data = pd.read_csv('appliance_sales.csv')

# Create figure with GridSpec layout: 2 rows, 2 cols
fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[2, 1])  # top row taller

# Plot 1: Full width on top (row 0, col span 2)
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(data['Quarter'], data['Fridge'], label='Fridge')
ax1.plot(data['Quarter'], data['Dishwasher'], label='Dishwasher')
ax1.plot(data['Quarter'], data['Washing Machine'], label='Washing Machine')
ax1.set_title('Product Sales Over Quarters')
ax1.set_xlabel('Quarters')
ax1.set_ylabel('Sales in Million $')
ax1.legend()
ax1.tick_params(axis='x', rotation=45)

# Plot 2: Bottom left (row 1, col 0) - Pie chart
ax2 = fig.add_subplot(gs[1, 0])
sales = data[['Fridge', 'Dishwasher', 'Washing Machine']].sum()
ax2.pie(sales, labels=sales.index, autopct='%1.1f%%', shadow=True, startangle=140)
ax2.set_title('Sales Distribution by Product')

# Plot 3: Bottom right (row 1, col 1) - Bar plot
ax3 = fig.add_subplot(gs[1, 1])
data.plot(kind='bar', x='Quarter', ax=ax3)
ax3.set_title('Sales by Quarter')
ax3.set_xlabel('Quarter')
ax3.set_ylabel('Sales in Million $')
ax3.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
