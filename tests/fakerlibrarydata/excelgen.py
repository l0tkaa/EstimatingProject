import os
from dotenv import load_dotenv
import pandas as pd
import random
from faker import Faker

fake = Faker()

# Define materials and base price per square foot
materials = ['Wood', 'Steel', 'Copper', 'Plastic', 'Aluminum', 'Glass', 'Brick', 'Concrete']
base_price_per_sqft = {
    'Wood': 2,    # $2 per square foot
    'Steel': 4,   # $4 per square foot
    'Copper': 3,  # $3 per square foot
    'Plastic': 1, # $1 per square foot
    'Aluminum': 5, # $5 per square foot
    'Glass': 3,   # $3 per square foot
    'Brick': 2,   # $2 per square foot
    'Concrete': 1.5  # $1.5 per square foot
}

# Folder path where files will be saved
folder_path = os.getenv(EXCEL_SAMPLES)

# Create the directory if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Function to create a DataFrame with random data
def create_sample_data():
    data = []
    for _ in range(10):  # 10 rows per file
        material = random.choice(materials)
        size_in_sqft = random.randint(10, 1000)  # Size in square feet (random from 10 to 1000)
        price_per_sqft = base_price_per_sqft[material]
        total_price = round(size_in_sqft * price_per_sqft, 2)  # Total price is based on size
        quantity = random.randint(1, 100)
        
        data.append({
            'Material': material,
            'Size (sqft)': size_in_sqft,
            'Price per SqFt': price_per_sqft,
            'Total Price': total_price,
            'Quantity': quantity,
            'Supplier': fake.company(),
            'Date': fake.date()
        })
    return pd.DataFrame(data)

# Generate 100 Excel files
for i in range(1, 101):
    df = create_sample_data()
    filename = f'materials_data_{i}.xlsx'
    file_path = os.path.join(folder_path, filename)
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f'Generated {file_path}')
