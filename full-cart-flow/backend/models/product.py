from utils.db import db
import datetime
 
class Product:
    @staticmethod
    def get_collection():
        return db.products
    
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
        # Return documents with ObjectId converted to string
        products = list(Product.get_collection().find(filter_query))
        for p in products:
            p['_id'] = str(p['_id'])
        return products
    
    @staticmethod
    def find_by_id(product_id):
        from bson import ObjectId
        try:
            # Convert string ID to ObjectId
            obj_id = ObjectId(product_id)
            product = Product.get_collection().find_one({'_id': obj_id})
            if product:
                product['_id'] = str(product['_id'])
            return product
        except:
            return None
