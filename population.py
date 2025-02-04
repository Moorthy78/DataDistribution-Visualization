#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "cfile.csv"  

try:
    df = pd.read_csv(file_path, skiprows=4)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Please check the path.")
    exit()

print("🔹 First 5 Rows:\n", df.head())

df = df.dropna(axis=1, how="all")  
latest_year = df.columns[-1]  

if 'Country Name' not in df.columns:
    print("Error: 'Country Name' column not found. Check dataset structure.")
    exit()

df = df[['Country Name', latest_year]].dropna()  
df.columns = ['Country', 'Population']  

df['Population'] = pd.to_numeric(df['Population'], errors='coerce')
df.dropna(subset=['Population'], inplace=True)

df_top10 = df.sort_values(by='Population', ascending=False).head(10)

if not df_top10.empty:
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Population', y='Country', data=df_top10, palette='coolwarm')
    plt.xlabel("Population")
    plt.ylabel("Country")
    plt.title("Top 10 Most Populated Countries (Latest Year)")
    plt.xscale('log')  
    plt.show()
else:
    print("No valid population data available for top 10 countries.")

if not df.empty:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Population'], bins=30, kde=True, color='blue')
    plt.xlabel("Population")
    plt.ylabel("Frequency")
    plt.title("Global Population Distribution")
    plt.xscale('log')  
    plt.show()
else:
    print("No valid population data available for histogram.")


# In[ ]:




