# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZbF9vA9dVLw_bu-20ApHzniaXa6k3aBW

## Data loading

Load the dataset "datasets.csv" into a pandas DataFrame.
"""

import pandas as pd

df = pd.read_csv('datasets.csv')
display(df.head())
print(df.shape)

"""## Data exploration

Explore the loaded dataset to understand its basic characteristics.

"""

# Data Types
print("Data Types:\n", df.dtypes)

# Missing Values
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
print("\nMissing Values:\n", missing_values)
print("\nMissing Value Percentage:\n", missing_percentage)

# Descriptive Statistics for Numerical Columns
numerical_cols = df.select_dtypes(include=['number'])
print("\nDescriptive Statistics for Numerical Columns:\n", numerical_cols.describe())

# Unique Values and Frequencies for Categorical Columns
categorical_cols = df.select_dtypes(include=['object'])
for col in categorical_cols.columns:
    print(f"\nUnique values and frequencies for {col}:\n{categorical_cols[col].value_counts()}")

# Shape of the DataFrame
print("\nShape of the DataFrame:", df.shape)

"""## Data cleaning

Clean the data by handling missing values and outliers in the `df` DataFrame.

"""

import numpy as np

# Impute missing values
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col] = df[col].fillna(df[col].median())
    elif df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode()[0])

# Outlier handling for 'price'
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df['price'] = np.clip(df['price'], lower_bound, upper_bound)

# Convert columns to numeric, handling errors
for col in ['bedrooms', 'beds', 'baths']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].fillna(df[col].median())

display(df.head())

"""## Data analysis

Perform descriptive statistics and analyze the distributions of variables in the cleaned dataset.  Calculate correlations between relevant numerical variables.

"""

import matplotlib.pyplot as plt
import seaborn as sns

# Descriptive Statistics
numerical_cols = df.select_dtypes(include=['number'])
print("Descriptive Statistics:\n", numerical_cols.describe())

# Distribution Analysis
plt.figure(figsize=(15, 10))
for i, col in enumerate(['price', 'minimum_nights', 'number_of_reviews', 'availability_365']):
    plt.subplot(2, 2, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()


# Correlation Matrix
correlation_matrix = numerical_cols.corr()
print("\nCorrelation Matrix:\n", correlation_matrix)

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.show()

"""## Data visualization

Visualize the key findings from the data analysis, focusing on distributions and correlations.

"""

import matplotlib.pyplot as plt
import seaborn as sns

# Histograms with KDE
plt.figure(figsize=(16, 8))
for i, col in enumerate(['price', 'minimum_nights', 'number_of_reviews', 'availability_365']):
    plt.subplot(2, 2, i + 1)
    sns.histplot(df[col], kde=True, bins=30, color='skyblue')  # Experiment with different bin sizes
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# Box plots
plt.figure(figsize=(16, 8))
for i, col in enumerate(['price', 'minimum_nights', 'number_of_reviews', 'availability_365']):
    plt.subplot(2, 2, i + 1)
    sns.boxplot(y=df[col], color='lightgreen')
    plt.title(f'Box Plot of {col}')
plt.tight_layout()
plt.show()

# Correlation matrix heatmap
numerical_cols = df.select_dtypes(include=['number'])
correlation_matrix = numerical_cols.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.show()

# Scatter plots for significant correlations (example)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='number_of_reviews', y='reviews_per_month', data=df, color='orange')
plt.title('Scatter Plot: Number of Reviews vs Reviews per Month')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='availability_365', y='price', data=df, color='purple')
plt.title('Scatter Plot: Availability vs Price')
plt.show()