import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("customer_churn.csv")

# Display basic information
print("Dataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle Missing Values
df.fillna(df.median(numeric_only=True), inplace=True)

# Identify Numerical Columns
numeric_columns = df.select_dtypes(include=np.number).columns

# Outlier Detection and Removal using IQR
for col in numeric_columns:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

# Churn Visualization
if "Churn" in df.columns:
    df["Churn"].value_counts().plot(kind="bar",
                                    color=["skyblue", "orange"])
    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")
    plt.show()

# Histograms
df[numeric_columns].hist(figsize=(10,8))
plt.suptitle("Distribution of Numerical Variables")
plt.show()

# Boxplot
df[numeric_columns].plot(kind='box',
                         figsize=(12,6))
plt.title("Boxplot for Outlier Detection")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df[numeric_columns].corr(),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("\nData Cleaning Completed Successfully.")