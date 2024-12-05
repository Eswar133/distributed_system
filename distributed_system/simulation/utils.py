import threading
from simulation.models import User, Product, Order

def insert_users():
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
        {"id": 4, "name": "David", "email": "david@example.com"},
        {"id": 5, "name": "Eve", "email": "eve@example.com"},
        {"id": 6, "name": "Frank", "email": "frank@example.com"},
        {"id": 7, "name": "Grace", "email": "grace@example.com"},
        {"id": 8, "name": "Alice", "email": "alice@example.com"},
        {"id": 9, "name": "Henry", "email": "henry@example.com"},
        {"id": 10, "name": "Jane", "email": "jane@example.com"},
    ]
    for user in users:
        User.objects.using('users_db').create(**user)

def insert_products():
    products = [
        {"id": 1, "name": "Laptop", "price": 1000.00},
        {"id": 2, "name": "Smartphone", "price": 700.00},
        {"id": 3, "name": "Headphones", "price": 150.00},
        {"id": 4, "name": "Monitor", "price": 300.00},
        {"id": 5, "name": "Keyboard", "price": 50.00},
        {"id": 6, "name": "Mouse", "price": 30.00},
        {"id": 7, "name": "Laptop", "price": 1000.00},
        {"id": 8, "name": "Smartwatch", "price": 250.00},
        {"id": 9, "name": "Gaming Chair", "price": 500.00},
        {"id": 10, "name": "Earbuds", "price": -50.00},
    ]
    for product in products:
        Product.objects.using('products_db').create(**product)

def insert_orders():
    orders = [
        {"id": 1, "user_id": 1, "product_id": 1, "quantity": 2},
        {"id": 2, "user_id": 2, "product_id": 2, "quantity": 1},
        {"id": 3, "user_id": 3, "product_id": 3, "quantity": 5},
        {"id": 4, "user_id": 4, "product_id": 4, "quantity": 1},
        {"id": 5, "user_id": 5, "product_id": 5, "quantity": 3},
        {"id": 6, "user_id": 6, "product_id": 6, "quantity": 4},
        {"id": 7, "user_id": 7, "product_id": 7, "quantity": 2},
        {"id": 8, "user_id": 8, "product_id": 8, "quantity": 0},
        {"id": 9, "user_id": 9, "product_id": 1, "quantity": -1},
        {"id": 10, "user_id": 10, "product_id": 11, "quantity": 2},
    ]
    for order in orders:
        Order.objects.using('orders_db').create(**order)

def simulate_insertions():
    threads = []
    for func in [insert_users, insert_products, insert_orders]:
        thread = threading.Thread(target=func)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
