import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data
data = pd.read_csv('movies.csv')

# Data cleaning and preparation
data['imdb_rating'] = pd.to_numeric(data['imdb_rating'], errors='coerce')
data['budget'] = pd.to_numeric(data['budget'], errors='coerce')
data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce')
data['release_year'] = pd.to_numeric(data['release_year'], errors='coerce')
data['studio'] = data['studio'].fillna('Unknown')
data['imdb_rating'] = data['imdb_rating'].fillna(0)

# --- Analysis 1: Movie count by industry ---
ind_count = data['industry'].value_counts()
plt.figure(figsize=(6,4))
ind_count.plot(kind='bar', color=['#1F77B4','#FF7F0E'])
plt.title('Number of Movies by Industry')
plt.xlabel('Industry')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('industry_count.png')
plt.close()

# --- Analysis 2: Average IMDb rating by industry ---
avg_rating = data.groupby('industry')['imdb_rating'].mean()
plt.figure(figsize=(6,4))
avg_rating.plot(kind='bar', color=['#2CA02C','#D62728'])
plt.title('Average IMDb Rating by Industry')
plt.xlabel('Industry')
plt.ylabel('Average IMDb Rating')
plt.tight_layout()
plt.savefig('avg_rating.png')
plt.close()

# --- Analysis 3: Top 5 movies by revenue (converted all to Millions) ---
def revenue_in_million(row):
    if row['unit'] == 'Millions':
        return row['revenue']
    elif row['unit'] == 'Thousands':
        return row['revenue'] / 1000
    elif row['unit'] == 'Billions':
        return row['revenue'] * 1000
    else:
        return row['revenue']
data['revenue_million'] = data.apply(revenue_in_million, axis=1)
top_revenue = data.sort_values('revenue_million', ascending=False)[['title','industry','release_year','revenue_million']].head(5)
plt.figure(figsize=(8,5))
plt.bar(top_revenue['title'], top_revenue['revenue_million'], color='#9467BD')
plt.title('Top 5 Movies by Revenue (Millions)')
plt.xlabel('Movie Title')
plt.ylabel('Revenue (Millions)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_revenue.png')
plt.close()

# --- Pie chart: Movie count by language ---
lang_count = data['language'].value_counts()
plt.figure(figsize=(7,7))
lang_count.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Movie Distribution by Language')
plt.ylabel('')
plt.tight_layout()
plt.savefig('language_pie.png')
plt.close()

print("Analysis & all charts complete! 🏁")
