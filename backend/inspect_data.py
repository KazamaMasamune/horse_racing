import pandas as pd

# Load the dataset
df = pd.read_csv('race-result-horse.csv')

# Set pandas display options to show more columns and avoid truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Display the first 5 rows and column names
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# Check the distribution of finishing_position
print("\nUnique finishing_position values:", df['finishing_position'].unique())
print("Number of rows per finishing_position:\n", df['finishing_position'].value_counts())
print("Number of winners (finishing_position == 1):", (df['finishing_position'] == 1).sum())
print("Data type of finishing_position:", df['finishing_position'].dtype)

# Check for any non-numeric values in finishing_position
print("\nSample of finishing_position values (first 10 rows):", df['finishing_position'].head(10).tolist())
