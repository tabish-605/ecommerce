from utils.db import init_db, db
from models.product import Product
import os
import datetime
 
# Initialize database without app context
init_db()
 
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
            "created_at": datetime.datetime.utcnow(),
            "updated_at": datetime.datetime.utcnow()
        },
        {
            "name": "Cotton T-Shirt",
            "price": 19.99,
            "description": "Comfortable cotton t-shirt for everyday wear",
"image": "https://example.com/tshirt.jpg",
            "category": "Clothing",
            "rating": 4.2,
            "stock": 100,
            "created_at": datetime.datetime.utcnow(),
            "updated_at": datetime.datetime.utcnow()
        },
        {
            "name": "Coffee Maker",
            "price": 49.99,
            "description": "Programmable coffee maker with thermal carafe",
"image": "https://example.com/coffeemaker.jpg",
            "category": "Home",
            "rating": 4.7,
            "stock": 30,
            "created_at": datetime.datetime.utcnow(),
            "updated_at": datetime.datetime.utcnow()
        },
        {
            "name": "JavaScript: The Good Parts",
            "price": 24.99,
            "description": "Classic book on JavaScript programming",
"image": "https://example.com/jsbook.jpg",
            "category": "Books",
            "rating": 4.8,
            "stock": 75,
            "created_at": datetime.datetime.utcnow(),
            "updated_at": datetime.datetime.utcnow()
        },
        {
            "name": "Smart Watch",
            "price": 199.99,
            "description": "Feature-rich smartwatch with health tracking",
"image": "https://example.com/smartwatch.jpg",
            "category": "Electronics",
            "rating": 4.6,
            "stock": 40,
            "created_at": datetime.datetime.utcnow(),
            "updated_at": datetime.datetime.utcnow()
        }
    ]
    
    try:
        # Clear existing products
        Product.get_collection().delete_many({})
        print('Existing products cleared')
        
        # Add seed products
        result = Product.get_collection().insert_many(sample_products)
        print(f'Inserted {len(result.inserted_ids)} products')
        
        # Create indexes
        Product.create_indexes()
        print('Indexes created')
        
    except Exception as e:
        print(f'Database seeding failed: {str(e)}')
 
if __name__ == '__main__':
    seed_products()
