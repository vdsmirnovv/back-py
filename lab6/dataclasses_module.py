from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    stock: int

@dataclass
class Customer:
    name: str
    email: str
    purchases: list

@dataclass
class Order:
    order_id: int
    product: Product
    quantity: int

def create_product(name, price, stock):
    return Product(name=name, price=price, stock=stock)

def update_stock(product, quantity):
    product.stock -= quantity
    return product

def list_products(products):
    return [product.name for product in products]

def customer_purchases():
    customer = Customer("Alice", "alice@example.com", [])
    product = Product("Laptop", 1200.0, 5)
    customer.purchases.append(product)
    return {customer.name: customer.purchases}

def create_order(order_id, product, quantity):
    return Order(order_id, product, quantity)