from flask import Blueprint, request, jsonify
from models.product import Product
 
products_bp = Blueprint('products', __name__)
 
@products_bp.route('/', methods=['GET'])
def get_products():
    try:
        # Get query parameters
        category = request.args.get('category')
        search = request.args.get('search')
        min_price = request.args.get('minPrice')
        max_price = request.args.get('maxPrice')
        
        # Build filter
        filter_query = {}
        if category:
            filter_query['category'] = category
        if search:
            filter_query['name'] = {'$regex': search, '$options': 'i'}
        if min_price:
            filter_query['price'] = {'$gte': float(min_price)}
        if max_price:
            if 'price' in filter_query:
                filter_query['price']['$lte'] = float(max_price)
            else:
                filter_query['price'] = {'$lte': float(max_price)}
        
        # Get products
        products = Product.find_all(filter_query)
        return jsonify({
            'success': True,
            'count': len(products),
            'data': products
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
 
@products_bp.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = Product.find_by_id(product_id)
        if not product:
            return jsonify({
                'success': False,
                'error': 'Product not found'
            }), 404
            
        return jsonify({
            'success': True,
            'data': product
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
