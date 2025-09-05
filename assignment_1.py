import pandas as pd
import numpy as np

df = pd.read_csv('./data/iowa.csv')

#Exploring the data
print(df.head())
print(df.keys())
print(df.describe())

# #Analysing the data variables
print(df['Category Name'].unique()) # Categorical data
print(df['Category Name'].value_counts())
print(df['Bottles Sold']) # Numerical data
print(df['Bottles Sold'].describe())

#Checking for missing data
na_values = df['Zip Code'].isna()
print(np.sum(na_values))

print(df.isnull().sum())

#Prediction Tools

'''
Sales Prediction Tools

Predict sales in Iowa across different zip codes or categories.
Identify peak sales days, such as weekends, holidays, or seasonal trends.
Forecast monthly sales for stores for the upcoming month.
Determine the most popular and least popular alcohol.
Identify the cheapest and most expensive alcohol available.

Pricing optimization tool: Assess whether retail price affects the number of bottles sold.

Stakeholders for the Prediction Tools

Sales managers and store managers: for inventory management and daily sales planning.
Marketing team: to optimize strategies.
Executives: for insights on overall revenue and business performance.

Helpful Additional Data

Customer-level data: demographics or quantity.
Promotions or discounts applied
'''