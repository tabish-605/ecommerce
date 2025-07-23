from flask import Blueprint, request, jsonify
from models.cart import Cart
 
cart_bp = Blueprint('cart', __name__)
 
@cart_bp.route('/<user_id>', methods=['GET'])
def get_cart(user_id):
    try:
        cart = Cart.get_cart(user_id)
        return jsonify({
            'success': True,
            'data': cart
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
 
@cart_bp.route('/<user_id>', methods=['POST'])
def update_cart(user_id):
    try:
        data = request.get_json()
        product_id = data.get('productId')
        quantity = int(data.get('quantity', 1))
        
        if not product_id:
            return jsonify({
                'success': False,
                'error': 'Product ID is required'
            }), 400
        
        cart = Cart.add_to_cart(user_id, product_id, quantity)
        if not cart:
            return jsonify({
                'success': False,
                'error': 'Product not found'
            }), 404
            
        return jsonify({
            'success': True,
            'data': cart
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
 
@cart_bp.route('/<user_id>/<product_id>', methods=['DELETE'])
def remove_from_cart(user_id, product_id):
    try:
        cart = Cart.remove_from_cart(user_id, product_id)
        if not cart:
            return jsonify({
                'success': False,
                'error': 'Cart not found'
            }), 404
            
        return jsonify({
            'success': True,
            'data': cart
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
