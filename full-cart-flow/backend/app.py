from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from routes.products import products_bp
from routes.cart import cart_bp
 
load_dotenv()
 
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": os.getenv('FRONTEND_URL', 'http://localhost:3000')}})
 
# Register blueprints
app.register_blueprint(products_bp, url_prefix='/api/products')
app.register_blueprint(cart_bp, url_prefix='/api/cart')
 
@app.route('/health')
def health_check():
    return 'OK'
 
if __name__ == '__main__':
app.run(host='0.0.0.0', port=os.getenv('PORT', 5000), debug=os.getenv('DEBUG', 'False') == 'True')
