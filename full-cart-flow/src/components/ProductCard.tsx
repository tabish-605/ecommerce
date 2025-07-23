import { Heart, Star, ShoppingCart } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Card, CardContent } from '@/components/ui/card';
import { Product } from '@/types/product';
import { useCart } from '@/contexts/CartContext';
import { useState } from 'react';

interface ProductCardProps {
  product: Product;
  onViewDetails?: (product: Product) => void;
}

export function ProductCard({ product, onViewDetails }: ProductCardProps) {
  const { addToCart } = useCart();
  const [isLiked, setIsLiked] = useState(false);
  const [isAddingToCart, setIsAddingToCart] = useState(false);

  const handleAddToCart = async (e: React.MouseEvent) => {
    e.stopPropagation();
    setIsAddingToCart(true);
    await new Promise(resolve => setTimeout(resolve, 300)); // Simulate API call
    addToCart(product);
    setIsAddingToCart(false);
  };

  const handleLike = (e: React.MouseEvent) => {
    e.stopPropagation();
    setIsLiked(!isLiked);
  };

  const discountPercentage = product.originalPrice 
    ? Math.round(((product.originalPrice - product.price) / product.originalPrice) * 100)
    : 0;

  return (
    <Card 
      className="group cursor-pointer overflow-hidden transition-smooth hover:shadow-hover hover:-translate-y-1 animate-scale-in"
      onClick={() => onViewDetails?.(product)}
    >
      <CardContent className="p-0">
        {/* Image container */}
        <div className="relative aspect-square overflow-hidden bg-muted/30">
          <img
            src={product.images[0]}
            alt={product.name}
            className="w-full h-full object-cover transition-smooth group-hover:scale-105"
          />
          
          {/* Badges */}
          <div className="absolute top-3 left-3 flex flex-col gap-1">
            {!product.inStock && (
              <Badge variant="destructive" className="text-xs">
                Out of Stock
              </Badge>
            )}
            {discountPercentage > 0 && (
              <Badge className="bg-accent text-accent-foreground text-xs">
                -{discountPercentage}%
              </Badge>
            )}
          </div>

          {/* Like button */}
          <Button
            variant="ghost"
            size="icon"
            className={`absolute top-3 right-3 bg-card/80 backdrop-blur-sm hover:bg-card transition-smooth ${
              isLiked ? 'text-red-500' : 'text-muted-foreground'
            }`}
            onClick={handleLike}
          >
            <Heart className={`w-4 h-4 ${isLiked ? 'fill-current' : ''}`} />
          </Button>

          {/* Quick add to cart - appears on hover */}
          <div className="absolute inset-x-3 bottom-3 opacity-0 group-hover:opacity-100 transition-smooth">
            <Button
              variant="cart"
              size="sm"
              className="w-full backdrop-blur-sm"
              onClick={handleAddToCart}
              disabled={!product.inStock || isAddingToCart}
            >
              <ShoppingCart className="w-4 h-4 mr-2" />
              {isAddingToCart ? 'Adding...' : 'Add to Cart'}
            </Button>
          </div>
        </div>

        {/* Product info */}
        <div className="p-4 space-y-3">
          {/* Brand and category */}
          <div className="flex items-center justify-between text-sm text-muted-foreground">
            <span>{product.brand}</span>
            <span>{product.category}</span>
          </div>

          {/* Product name */}
          <h3 className="font-semibold text-foreground group-hover:text-primary transition-smooth line-clamp-2">
            {product.name}
          </h3>

          {/* Rating */}
          <div className="flex items-center gap-2">
            <div className="flex items-center gap-1">
              <Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />
              <span className="text-sm font-medium">{product.rating}</span>
            </div>
            <span className="text-sm text-muted-foreground">
              ({product.reviewCount} reviews)
            </span>
          </div>

          {/* Price */}
          <div className="flex items-center gap-2">
            <span className="text-xl font-bold text-foreground">
              ${product.price}
            </span>
            {product.originalPrice && (
              <span className="text-sm text-muted-foreground line-through">
                ${product.originalPrice}
              </span>
            )}
          </div>

          {/* Stock status */}
          <div className="text-sm">
            {product.inStock ? (
              <span className="text-accent">
                {product.stockCount > 10 ? 'In Stock' : `Only ${product.stockCount} left`}
              </span>
            ) : (
              <span className="text-destructive">Out of Stock</span>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  );
}