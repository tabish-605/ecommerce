import { ArrowRight, ShoppingBag, Star, Zap } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import phone1 from '@/assets/phone-1.jpg';
import laptop1 from '@/assets/laptop-1.jpg';
import headphones1 from '@/assets/headphones-1.jpg';

export function Hero() {
  return (
    <section className="relative overflow-hidden bg-gradient-background">
      {/* Background pattern */}
      <div className="absolute inset-0 bg-grid-pattern opacity-5"></div>
      
      <div className="container mx-auto px-4 py-16 lg:py-24">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left content */}
          <div className="space-y-8 animate-slide-up">
            <div className="space-y-4">
              <Badge className="bg-accent/10 text-accent border-accent/20">
                <Star className="w-3 h-3 mr-1" />
                #1 Electronics Store
              </Badge>
              
              <h1 className="text-4xl lg:text-6xl font-bold text-foreground leading-tight">
                Premium Tech
                <span className="bg-gradient-primary bg-clip-text text-transparent block">
                  Delivered Fast
                </span>
              </h1>
              
              <p className="text-lg text-muted-foreground max-w-lg">
                Discover the latest smartphones, laptops, and gadgets from top brands. 
                Get free shipping on orders over $99 and enjoy our 30-day return policy.
              </p>
            </div>

            {/* Stats */}
            <div className="flex items-center gap-8">
              <div className="text-center">
                <div className="text-2xl font-bold text-foreground">50K+</div>
                <div className="text-sm text-muted-foreground">Happy Customers</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-foreground">4.9</div>
                <div className="text-sm text-muted-foreground">Average Rating</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-foreground">24/7</div>
                <div className="text-sm text-muted-foreground">Support</div>
              </div>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4">
              <Button size="lg" className="group">
                <ShoppingBag className="w-5 h-5 mr-2" />
                Shop Now
                <ArrowRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-smooth" />
              </Button>
              
              <Button variant="outline" size="lg">
                View Categories
              </Button>
            </div>

            {/* Features */}
            <div className="flex flex-wrap gap-4 pt-4">
              <div className="flex items-center gap-2 text-sm text-muted-foreground">
                <Zap className="w-4 h-4 text-accent" />
                Free shipping over $99
              </div>
              <div className="flex items-center gap-2 text-sm text-muted-foreground">
                <Zap className="w-4 h-4 text-accent" />
                30-day returns
              </div>
              <div className="flex items-center gap-2 text-sm text-muted-foreground">
                <Zap className="w-4 h-4 text-accent" />
                2-year warranty
              </div>
            </div>
          </div>

          {/* Right content - Featured product showcase */}
          <div className="relative">
            {/* Floating product cards */}
            <div className="relative h-[500px] animate-float">
              {/* Main product card */}
              <div className="absolute top-0 right-0 w-64 bg-card rounded-2xl p-6 shadow-hover border border-border">
                <div className="aspect-square bg-muted/30 rounded-lg mb-4 overflow-hidden">
                  <img
                    src={phone1}
                    alt="Featured product"
                    className="w-full h-full object-cover"
                  />
                </div>
                <h3 className="font-semibold text-foreground mb-2">ProMax Smartphone</h3>
                <div className="flex items-center justify-between">
                  <span className="text-xl font-bold text-foreground">$999</span>
                  <div className="flex items-center gap-1">
                    <Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />
                    <span className="text-sm">4.8</span>
                  </div>
                </div>
              </div>

              {/* Secondary product cards */}
              <div className="absolute bottom-0 left-0 w-48 bg-card rounded-xl p-4 shadow-card border border-border animate-float" style={{ animationDelay: '1s' }}>
                <div className="aspect-square bg-muted/30 rounded-lg mb-3 overflow-hidden">
                  <img
                    src={laptop1}
                    alt="Featured product 2"
                    className="w-full h-full object-cover"
                  />
                </div>
                <h4 className="font-medium text-foreground text-sm mb-1">UltraBook Pro</h4>
                <span className="text-lg font-bold text-foreground">$1,499</span>
              </div>

              <div className="absolute top-20 left-8 w-40 bg-card rounded-xl p-3 shadow-card border border-border animate-float" style={{ animationDelay: '2s' }}>
                <div className="aspect-square bg-muted/30 rounded-lg mb-2 overflow-hidden">
                  <img
                    src={headphones1}
                    alt="Featured product 3"
                    className="w-full h-full object-cover"
                  />
                </div>
                <h4 className="font-medium text-foreground text-xs mb-1">SoundMax</h4>
                <span className="text-sm font-bold text-foreground">$299</span>
              </div>
            </div>

            {/* Decorative elements */}
            <div className="absolute -top-8 -right-8 w-16 h-16 bg-gradient-primary rounded-full opacity-20 animate-float"></div>
            <div className="absolute -bottom-4 -left-4 w-12 h-12 bg-gradient-secondary rounded-full opacity-20 animate-float" style={{ animationDelay: '3s' }}></div>
          </div>
        </div>
      </div>
    </section>
  );
}