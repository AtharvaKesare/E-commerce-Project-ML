import pandas as pd

# Load data
df = pd.read_csv(r"D:\ML E-commerce Project\ecommerce_reviews.csv")


# 1. Basic Inspection
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

# 2. Remove duplicates (if any)
df = df.drop_duplicates()

# 3. Strip whitespace from string columns
for col in ['Product_Name', 'Category', 'Brand', 'Review_Text', 'Sentiment']:
    df[col] = df[col].astype(str).str.strip()

# 4. Handle missing values - drop rows with missing key info
df = df.dropna(subset=['Product_Name', 'Category', 'Rating', 'Review_Text'])

# 5. Ensure correct data types
df['Rating'] = df['Rating'].astype(float)
df['Helpful_Votes'] = df['Helpful_Votes'].astype(int)

# 6. Save cleaned data (optional)
df.to_csv('ecommerce_reviews_clean.csv', index=False)
print('Cleaned dataset created!')
