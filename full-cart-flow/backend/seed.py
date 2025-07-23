from utils.db import init_db, db
from models.product import Product
import datetime
import os
from datetime import datetime, UTC
# Initialize database
try:
    init_db()
    print("Database initialized successfully")
except Exception as e:
    print(f"Database initialization failed: {str(e)}")
    exit(1)
 
def seed_products():
    sample_products = [
        {
            "name": "Wireless Headphones",
            "price": 89.99,
            "description": "Premium noise-cancelling wireless headphones",
"image": "https://example.com/headphones.jpg",
            "category": "Electronics",
            "rating": 4.5,
            "stock": 50,
            "created_at": datetime.now(UTC),
            "updated_at": datetime.now(UTC)
        },
        {
            "name": "Cotton T-Shirt",
            "price": 19.99,
            "description": "Comfortable cotton t-shirt for everyday wear",
"image": "https://example.com/tshirt.jpg",
            "category": "Clothing",
            "rating": 4.2,
            "stock": 100,
            "created_at": datetime.now(UTC),
            "updated_at": datetime.now(UTC)
        },
        {
            "name": "Coffee Maker",
            "price": 49.99,
            "description": "Programmable coffee maker with thermal carafe",
"image": "https://example.com/coffeemaker.jpg",
            "category": "Home",
            "rating": 4.7,
            "stock": 30,
            "created_at": datetime.now(UTC),
            "updated_at": datetime.now(UTC)
        },
        {
            "name": "JavaScript: The Good Parts",
            "price": 24.99,
            "description": "Classic book on JavaScript programming",
"image": "https://example.com/jsbook.jpg",
            "category": "Books",
            "rating": 4.8,
            "stock": 75,
            "created_at": datetime.now(UTC),
            "updated_at": datetime.now(UTC)
        },
        {
            "name": "Smart Watch",
            "price": 199.99,
            "description": "Feature-rich smartwatch with health tracking",
"image": "https://example.com/smartwatch.jpg",
            "category": "Electronics",
            "rating": 4.6,
            "stock": 40,
            "created_at": datetime.now(UTC),
            "updated_at": datetime.now(UTC)
        }
    ]
    
    try:
        # Clear existing products
        Product.get_collection().delete_many({})
        print('Existing products cleared')
        
        # Add seed products
        result = Product.get_collection().insert_many(sample_products)
        print(f'Inserted {len(result.inserted_ids)} products')
        
        return True
    except Exception as e:
        print(f'Database seeding failed: {str(e)}')
        return False
 
if __name__ == '__main__':
    if seed_products():
        print("Database seeding completed successfully")
    else:
        print("Database seeding failed")
