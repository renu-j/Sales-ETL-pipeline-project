import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def load_data(df: pd.DataFrame) -> None:
    """
    Load a pandas DataFrame into PostgreSQL 'sales' table
    Args:
        df (pandas.DataFrame): Cleaned sales data
    """
    DB_USER = 'postgres'
    DB_PASSWORD = quote_plus('renu@123')  # safely encode special chars
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = 'sales_db'

    # Database connection string
    conn_str = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(conn_str)

    # Load data into PostgreSQL
    df.to_sql('sales', engine, if_exists='replace', index=False)
    print("Data loaded into PostgreSQL successfully!")

# Optional: Test the function if run directly
if __name__ == "__main__":
    print("This script is part of ETL and should be called from run_etl.py")
