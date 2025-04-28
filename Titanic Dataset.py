# Titanic Dataset - Exploratory Data Analysis (EDA)

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
sns.set(style="whitegrid")

# 2. Load the Dataset
df = sns.load_dataset('titanic')
df.head()

# 3. Data Overview
print("Shape of the dataset:", df.shape)
print("\nInfo about the dataset:")
df.info()
print("\nSummary Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Univariate Analysis

# 4.1 Categorical Features
plt.figure(figsize=(10,5))
sns.countplot(x='sex', data=df)
plt.title('Count of Passengers by Gender')
plt.show()

# 4.2 Passenger Class
plt.figure(figsize=(10,5))
sns.countplot(x='class', data=df)
plt.title('Passenger Class Distribution')
plt.show()

# 4.3 Numerical Features: Age
plt.figure(figsize=(10,5))
sns.histplot(df['age'].dropna(), kde=True, bins=30)
plt.title('Distribution of Age')
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(y='age', data=df)
plt.title('Boxplot of Age')
plt.show()

# 5. Bivariate/Multivariate Analysis

# 5.1 Survival by Gender
plt.figure(figsize=(10,5))
sns.countplot(x='sex', hue='survived', data=df)
plt.title('Survival Count by Gender')
plt.show()

# 5.2 Survival by Class
plt.figure(figsize=(10,5))
sns.countplot(x='class', hue='survived', data=df)
plt.title('Survival Count by Class')
plt.show()

# 5.3 Age vs Survival
plt.figure(figsize=(10,5))
sns.histplot(data=df, x='age', hue='survived', kde=True, element="step")
plt.title('Age Distribution by Survival')
plt.show()

# 5.4 Correlation Heatmap
plt.figure(figsize=(12,8))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 6. Handling Missing Values

# Filling missing 'age' with median
df['age'].fillna(df['age'].median(), inplace=True)

# Dropping 'deck' column (too many missing values)
df.drop(columns=['deck'], inplace=True)

# Checking Missing Values again
print(df.isnull().sum())

# 7. Summary of Key Findings

print("""
- There are more male passengers than female passengers on the Titanic.
- Most passengers belonged to 3rd class.
- Age distribution shows most passengers were between 20-30 years.
- Female passengers had a much higher survival rate compared to males.
- First-class passengers had a better survival rate compared to other classes.
- Fare and Passenger Class have some correlation with survival.
""")
