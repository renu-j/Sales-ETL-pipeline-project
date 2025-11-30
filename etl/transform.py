# etl/transform.py

import pandas as pd

def transform_data(df):
    """
    Transform raw sales DataFrame to clean and consistent format.
    - Remove duplicates
    - Fill missing values
    - Fix data types
    - Fix dates
    - Calculate total_sale
    """
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing product_name and category with 'Unknown'
    df['product_name'] = df['product_name'].fillna('Unknown')
    df['category'] = df['category'].fillna('Unknown')

    # Ensure 'price' and 'quantity' are numeric
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0)

    # Convert 'sale_date' to datetime, coerce errors
    df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')

    # Drop rows where date conversion failed
    df = df.dropna(subset=['sale_date'])

    # Calculate total_sale
    df['total_sale'] = df['price'] * df['quantity']

    # Return the cleaned DataFrame
    return df