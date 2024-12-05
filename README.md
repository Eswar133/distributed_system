# Testing Your Django Distributed System

Follow this guide to test your Django application and ensure the task is completed successfully.

## Access SQLite Databases

### Using SQLite Command-Line Tool
1. Open a terminal or command prompt.
2. Navigate to the directory containing your `users.db`, `products.db`, and `orders.db`.
3. Run the SQLite client for a specific database:
   ```bash
   sqlite3 users.db
   ```
4. Inside the SQLite prompt, list tables and query data:
   ```sql
   .tables
   SELECT * FROM simulation_user;
   ```
5. Exit the SQLite client:
   ```sql
   .quit
   ```

---

## Access Data via Django Shell

1. Start the Django shell:
   ```bash
   python manage.py shell
   ```
2. Import models:
   ```python
   from simulation.models import User, Product, Order
   ```
3. Query data using Django ORM:

   **Fetch and Print Users:**
   ```python
   users = User.objects.using('users_db').all()
   for user in users:
       print(user.id, user.name, user.email)
   ```

   **Fetch and Print Products:**
   ```python
   products = Product.objects.using('products_db').all()
   for product in products:
       print(product.id, product.name, product.price)
   ```

   **Fetch and Print Orders:**
   ```python
   orders = Order.objects.using('orders_db').all()
   for order in orders:
       print(order.id, order.user_id, order.product_id, order.quantity)
   ```
4. Exit the Django shell:
   ```python
   exit()
   ```

---

## Debugging Common Issues

### Syntax Errors in the Django Shell
- **Issue:** Typing SQL commands (e.g., `SELECT * FROM simulation_user;`) in the Django shell causes `SyntaxError`.
- **Solution:** Use Python ORM commands in the Django shell or SQLite client for direct SQL queries.

### Missing Records in the Database
- **Check Database Files:** Ensure `users.db`, `products.db`, and `orders.db` exist in your project directory.
- **Check Insertions:** Rerun your custom management command to insert data:
  ```bash
  python manage.py run_simulation
  ```

---

## Automating Tests

Create automated tests to verify your implementation programmatically:

1. Add tests in `simulation/tests.py`:
   ```python
   from django.test import TestCase
   from simulation.models import User, Product, Order

   class DistributedSystemTest(TestCase):
       def test_user_insertion(self):
           users = User.objects.using('users_db').all()
           self.assertEqual(len(users), 10)
           self.assertEqual(users[0].name, "Alice")

       def test_product_insertion(self):
           products = Product.objects.using('products_db').all()
           self.assertEqual(len(products), 10)
           self.assertEqual(products[0].price, 1000.00)

       def test_order_insertion(self):
           orders = Order.objects.using('orders_db').all()
           self.assertEqual(len(orders), 10)
           self.assertEqual(orders[0].quantity, 2)
   ```

2. Run the tests:
   ```bash
   python manage.py test simulation
   ```

---

## Expected Outputs

### Example Output from Django Shell
If records exist in the database, the output for users might look like this:
```plaintext
1 Alice alice@example.com
2 Bob bob@example.com
3 Charlie charlie@example.com
...
```

### Output After Running Simulation
Run the simulation command:
```bash
python manage.py run_simulation
```
Expected output:
```plaintext
Simultaneous insertions completed!
```

---

Follow this guide to test and validate your implementation. Let me know if you encounter any issues!
