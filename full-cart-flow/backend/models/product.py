from utils.db import mongo
import datetime
 
class Product:
    @staticmethod
    def get_collection():
        return mongo.db.products
    
    @staticmethod
    def create_indexes():
        Product.get_collection().create_index("name")
        Product.get_collection().create_index("category")
    
    @staticmethod
    def create_product(data):
        product = {
            'name': data['name'],
            'price': float(data['price']),
            'description': data.get('description', ''),
            'image': data.get('image', ''),
            'category': data.get('category', 'Other'),
            'rating': float(data.get('rating', 0)),
            'stock': int(data.get('stock', 0)),
            'created_at': datetime.datetime.utcnow(),
            'updated_at': datetime.datetime.utcnow()
        }
        return Product.get_collection().insert_one(product)
    
    @staticmethod
    def find_all(filter_query=None):
        return list(Product.get_collection().find(filter_query, {'_id': 0}))
    
    @staticmethod
    def find_by_id(product_id):
        return Product.get_collection().find_one({'id': product_id}, {'_id': 0})
 
