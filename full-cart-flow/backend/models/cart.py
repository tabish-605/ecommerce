from utils.db import db
import datetime
from .product import Product
 
class Cart:
    @staticmethod
    def get_collection():
        return db.carts
    
    @staticmethod
    def create_indexes():
        Cart.get_collection().create_index("user_id")
    
    @staticmethod
    def get_cart(user_id):
        cart = Cart.get_collection().find_one({'user_id': user_id})
        if not cart:
            return {'user_id': user_id, 'items': [], 'total_price': 0.0}
        return cart
    
    @staticmethod
    def add_to_cart(user_id, product_id, quantity):
        # Get product
        product = Product.get_collection().find_one({'id': product_id})
        if not product:
            return None
        
        # Get or create cart
        cart = Cart.get_collection().find_one({'user_id': user_id})
        if not cart:
            cart = {
                'user_id': user_id,
                'items': [],
                'total_price': 0.0
            }
            result = Cart.get_collection().insert_one(cart)
            cart['_id'] = result.inserted_id
        else:
            cart['_id'] = str(cart['_id'])
        
        # Update cart items
        item_exists = False
        for item in cart['items']:
            if item['product_id'] == product_id:
                item['quantity'] += quantity
                item_exists = True
                break
        
        if not item_exists:
            cart['items'].append({
                'product_id': product_id,
                'quantity': quantity,
                'price': product['price']
            })
        
        # Calculate total price
        cart['total_price'] = sum(
            item['price'] * item['quantity'] for item in cart['items']
        )
        
        # Update cart in database
        Cart.get_collection().update_one(
            {'user_id': user_id},
            {'$set': {
                'items': cart['items'],
                'total_price': cart['total_price'],
                'updated_at': datetime.datetime.utcnow()
            }},
            upsert=True
        )
        
        return cart
    
    @staticmethod
    def remove_from_cart(user_id, product_id):
        cart = Cart.get_collection().find_one({'user_id': user_id})
        if not cart:
            return None
        
        # Remove item
        cart['items'] = [
            item for item in cart['items']
            if item['product_id'] != product_id
        ]
        
        # Calculate total price
        cart['total_price'] = sum(
            item['price'] * item['quantity'] for item in cart['items']
        )
        
        # Update cart
        Cart.get_collection().update_one(
            {'user_id': user_id},
            {'$set': {
                'items': cart['items'],
                'total_price': cart['total_price'],
                'updated_at': datetime.datetime.utcnow()
            }}
        )
        
        return cart
