from app import app
from utils.db import init_db
from models.product import Product
import json
import os
 
# Initialize app context
app.app_context().push()
init_db(app)
 
# Seed products
def seed_products():
    sample_products = [
        {
            "id": "1",
            "name": "Wireless Headphones",
            "price": 89.99,
            "description": "Premium noise-cancelling wireless headphones",
"image": "https://example.com/headphones.jpg",
            "category": "Electronics",
            "rating": 4.5,
            "stock": 50
        },
        {
            "id": "2",
            "name": "Cotton T-Shirt",
            "price": 19.99,
            "description": "Comfortable cotton t-shirt for everyday wear",
"image": "https://example.com/tshirt.jpg",
            "category": "Clothing",
            "rating": 4.2,
            "stock": 100
        },
        {
            "id": "3",
            "name": "Coffee Maker",
            "price": 49.99,
            "description": "Programmable coffee maker with thermal carafe",
"image": "https://example.com/coffeemaker.jpg",
            "category": "Home",
            "rating": 4.7,
            "stock": 30
        },
        {
            "id": "4",
            "name": "JavaScript: The Good Parts",
            "price": 24.99,
            "description": "Classic book on JavaScript programming",
"image": "https://example.com/jsbook.jpg",
            "category": "Books",
            "rating": 4.8,
            "stock": 75
        },
        {
            "id": "5",
            "name": "Smart Watch",
            "price": 199.99,
            "description": "Feature-rich smartwatch with health tracking",
"image": "https://example.com/smartwatch.jpg",
            "category": "Electronics",
            "rating": 4.6,
            "stock": 40
        }
    ]
    
    # Clear existing data
    Product.get_collection().delete_many({})
    
    # Insert new products
    result = Product.get_collection().insert_many(sample_products)
    print(f"Inserted {len(result.inserted_ids)} products")
 
if __name__ == '__main__':
    seed_products()
