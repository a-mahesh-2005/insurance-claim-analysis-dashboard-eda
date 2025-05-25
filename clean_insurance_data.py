import pandas as pd

# Load the raw dataset
df = pd.read_csv("insurance_data.csv")

# Drop the 'index' column
df.drop(columns=['index'], inplace=True)

# Fill missing 'age' values with median
df['age'].fillna(df['age'].median(), inplace=True)

# Fill missing 'region' values with mode
df['region'].fillna(df['region'].mode()[0], inplace=True)

# Remove duplicate rows, if any
df.drop_duplicates(inplace=True)

# Save cleaned data to new CSV file
df.to_csv("insurance_data_cleaned.csv", index=False)

print("Data cleaning complete. File saved as 'insurance_data_cleaned.csv'")
