import { Product } from '../types/product';
import phone1 from '../assets/phone-1.jpg';
import laptop1 from '../assets/laptop-1.jpg';
import headphones1 from '../assets/headphones-1.jpg';
import watch1 from '../assets/watch-1.jpg';

export const products: Product[] = [
  {
    id: '1',
    name: 'ProMax Smartphone',
    description: 'Latest flagship smartphone with advanced camera system, 5G connectivity, and all-day battery life. Features a stunning 6.7-inch OLED display and premium build quality.',
    price: 999,
    originalPrice: 1199,
    images: [phone1],
    category: 'Smartphones',
    brand: 'TechCorp',
    inStock: true,
    stockCount: 45,
    rating: 4.8,
    reviewCount: 324,
    tags: ['5G', 'Camera', 'Premium', 'Flagship'],
    specs: {
      'Display': '6.7" OLED',
      'Storage': '256GB',
      'RAM': '8GB',
      'Camera': '108MP Triple',
      'Battery': '4500mAh',
      'OS': 'Android 14'
    }
  },
  {
    id: '2',
    name: 'UltraBook Pro',
    description: 'Professional laptop with M2 chip, 16GB RAM, and 512GB SSD. Perfect for creative professionals and power users who demand performance and portability.',
    price: 1499,
    images: [laptop1],
    category: 'Laptops',
    brand: 'TechCorp',
    inStock: true,
    stockCount: 23,
    rating: 4.9,
    reviewCount: 156,
    tags: ['Professional', 'M2 Chip', 'Portable', 'Creative'],
    specs: {
      'Processor': 'M2 Chip',
      'RAM': '16GB',
      'Storage': '512GB SSD',
      'Display': '14" Retina',
      'Graphics': 'Integrated',
      'Weight': '3.0 lbs'
    }
  },
  {
    id: '3',
    name: 'SoundMax Wireless Headphones',
    description: 'Premium over-ear headphones with active noise cancellation, 30-hour battery life, and studio-quality sound. Experience music like never before.',
    price: 299,
    originalPrice: 399,
    images: [headphones1],
    category: 'Audio',
    brand: 'AudioTech',
    inStock: true,
    stockCount: 67,
    rating: 4.7,
    reviewCount: 892,
    tags: ['Wireless', 'Noise Cancelling', 'Premium', 'Studio Quality'],
    specs: {
      'Driver': '40mm Dynamic',
      'Battery': '30 hours',
      'Connectivity': 'Bluetooth 5.2',
      'Weight': '250g',
      'Frequency': '20Hz-20kHz',
      'Impedance': '32 Ohm'
    }
  },
  {
    id: '4',
    name: 'FitTracker Pro',
    description: 'Advanced fitness smartwatch with health monitoring, GPS tracking, and 7-day battery life. Track your fitness goals and stay connected on the go.',
    price: 399,
    images: [watch1],
    category: 'Wearables',
    brand: 'FitTech',
    inStock: true,
    stockCount: 34,
    rating: 4.6,
    reviewCount: 445,
    tags: ['Fitness', 'GPS', 'Health', 'Smartwatch'],
    specs: {
      'Display': '1.4" AMOLED',
      'Battery': '7 days',
      'GPS': 'Built-in',
      'Water Rating': '50m',
      'Sensors': 'Heart Rate, SpO2',
      'Connectivity': 'Bluetooth, WiFi'
    }
  },
  {
    id: '5',
    name: 'Gaming Console X',
    description: 'Next-generation gaming console with 4K graphics, ray tracing, and ultra-fast SSD. Experience gaming at its finest with exclusive titles.',
    price: 499,
    images: [phone1], // Placeholder
    category: 'Gaming',
    brand: 'GameTech',
    inStock: false,
    stockCount: 0,
    rating: 4.9,
    reviewCount: 1203,
    tags: ['Gaming', '4K', 'Ray Tracing', 'Next-Gen'],
    specs: {
      'Graphics': 'Custom GPU',
      'CPU': '8-core AMD',
      'Storage': '1TB SSD',
      'Memory': '16GB GDDR6',
      'Output': '4K HDR',
      'Ray Tracing': 'Hardware'
    }
  },
  {
    id: '6',
    name: 'Smart Home Hub',
    description: 'Central control hub for your smart home devices. Voice control, automation, and seamless integration with all major smart home platforms.',
    price: 149,
    images: [laptop1], // Placeholder
    category: 'Smart Home',
    brand: 'SmartTech',
    inStock: true,
    stockCount: 78,
    rating: 4.5,
    reviewCount: 267,
    tags: ['Smart Home', 'Voice Control', 'Automation', 'Hub'],
    specs: {
      'Connectivity': 'WiFi, Zigbee, Z-Wave',
      'Voice': 'Alexa, Google',
      'Ports': '4 USB, Ethernet',
      'Range': '50m',
      'Compatibility': 'Universal',
      'Display': '7" Touchscreen'
    }
  }
];