import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create a "Dirty" Dataset with missing values, duplicates, and inconsistencies
np.random.seed(42)
data = {
    'CustomerID': [101, 102, 103, 104, 102, 105, 106, 107, 108, 108], # Contains a duplicate ID (102, 108)
    'Customer_Name': ['Alice', 'Bob', 'Charlie', 'David', 'Bob', 'Eve', 'Frank', 'Grace', 'Hannah', 'Hannah'],
    'Age': [25, 30, np.nan, 22, 30, 29, 35, np.nan, 40, 40], # Contains missing Age values (NaN)
    'Annual_Income_k$': [50, 65, 80, np.nan, 65, 45, 90, 120, 55, 55], # Contains missing Income
    'Spending_Score': [70, 45, 60, 85, 45, 50, 30, 95, 60, 60]
}

df = pd.DataFrame(data)

# Save the raw dirty dataset
df.to_csv('raw_messy_data.csv', index=False)
print("Raw Messy Dataset Created & Saved!")

# 2. Automated Data Cleaning Process
# Step A: Remove Duplicate rows
df_cleaned = df.drop_duplicates().copy()

# Step B: Handle Missing Values (Impute Age with median, Income with median)
df_cleaned['Age'] = df_cleaned['Age'].fillna(df_cleaned['Age'].median())
df_cleaned['Annual_Income_k$'] = df_cleaned['Annual_Income_k$'].fillna(df_cleaned['Annual_Income_k$'].median())

# Save the cleaned dataset as an automated report file
df_cleaned.to_csv('cleaned_automated_report.csv', index=False)
print("Data Cleaning Completed! Cleaned Report Saved.")

# 3. Automated Reporting & Visualization Summary
print("\n--- Cleaned Data Summary ---")
print(df_cleaned.describe())

# Generate a visual summary chart
plt.figure(figsize=(8, 5))
plt.scatter(df_cleaned['Annual_Income_k$'], df_cleaned['Spending_Score'], color='purple', alpha=0.7, edgecolors='k')
plt.title('Automated Report: Annual Income vs Spending Score')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.grid(True)
plt.savefig('automated_report_chart.png')
print("\nAutomated Summary Chart Saved as 'automated_report_chart.png'!")