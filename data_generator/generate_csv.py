import pandas as pd
import random
from faker import Faker
import os

fake = Faker()
data_folder = '../data'

if not os.path.exists(data_folder):
    os.makedirs(data_folder)

products = ['Milk', 'Eggs', 'Bread', 'Juice', 'Rice', 'Butter', 'Cheese', 'Chocolate', 'Apple', 'Orange']
categories = ['Dairy','Bakery','Beverages','Grains','Snacks','Fruits']

def generate_sales_data(store_id, rows=20):
    data = []

    for _ in range(rows):
        product = random.choice(products)
        category = random.choice(categories)
        price = round(random.uniform(1.0, 20.0), 2)
        quantity = random.randint(1, 5)

        if random.random() < 0.1:
            product = None
        if random.random() < 0.1:
            category = None

        if random.random() < 0.1:
            sale_date = fake.date_between(start_date='-30d', end_date='today').strftime('%d-%m-%Y')
        else:
            sale_date = fake.date_between(start_date='-30d', end_date='today')

        data.append([store_id, product, category, price, quantity, sale_date])

    if random.random() < 0.2:
        data.append(random.choice(data))

    df = pd.DataFrame(
        data,
        columns=['store_id', 'product_name', 'category', 'price', 'quantity', 'sale_date']
    )

    return df

#  Save CSV files for 3 stores
for store_id in range(1, 4):
    df = generate_sales_data(store_id)
    output_path = f"{data_folder}/store_{store_id}_sales.csv"
    df.to_csv(output_path, index=False)
    print(f"Generated: {output_path}")
