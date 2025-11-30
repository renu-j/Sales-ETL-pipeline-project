# etl/run_etl.py

# This script runs the full ETL pipeline: extract -> transform -> load

from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl():
    # Step 1: Extract raw data from CSV files
    print("Extracting data...")
    raw_data = extract_data()
    print(f"Extracted {len(raw_data)} rows.")

    # Step 2: Transform the data
    print("Transforming data...")
    clean_data = transform_data(raw_data)
    print(f"Transformed data has {len(clean_data)} rows.")

    # Step 3: Load data into PostgreSQL
    print("Loading data into PostgreSQL...")
    load_data(clean_data)
    print("ETL pipeline completed successfully!")

# This ensures the ETL runs only when this script is executed directly
if __name__ == "__main__":
    run_etl()
