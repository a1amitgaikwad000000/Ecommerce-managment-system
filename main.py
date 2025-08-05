from abc import ABC, abstractmethod

# -----------------------------
# Abstract Class for User
# -----------------------------
class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_menu(self):
        pass

# -----------------------------
# Product Class
# -----------------------------
class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, qty):
        self.stock -= qty

# -----------------------------
# Admin Class
# -----------------------------
class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"✅ {product.name} added successfully.")

    def remove_product(self, pid):
        self.products = [p for p in self.products if p.pid != pid]
        print(f"🗑️ Product ID {pid} removed.")

    def show_products(self):
        if not self.products:
            print("📭 No products available.")
            return
        print("\n📦 Available Products:")
        for p in self.products:
            print(f"ID: {p.pid} | {p.name} | ₹{p.price} | Stock: {p.stock}")

    def show_menu(self):
        print(f"\n👨‍💼 Admin: {self.name}")
        while True:
            print("\n1. Add Product\n2. Remove Product\n3. Show Products\n4. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                pid = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock: "))
                product = Product(pid, name, price, stock)
                self.add_product(product)
            elif choice == '2':
                pid = int(input("Enter Product ID to remove: "))
                self.remove_product(pid)
            elif choice == '3':
                self.show_products()
            elif choice == '4':
                break
            else:
                print("❌ Invalid choice")

# -----------------------------
# Customer Class
# -----------------------------
class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart.append((product, quantity))
            print(f"🛒 {product.name} x {quantity} added to cart.")
        else:
            print(f"❌ Only {product.stock} in stock for {product.name}.")

    def view_cart(self):
        if not self.cart:
            print("🛒 Your cart is empty.")
            return
        print(f"\n🛒 Cart for {self.name}")
        for item, qty in self.cart:
            print(f"{item.name} - Qty: {qty} - ₹{item.price * qty}")

    def checkout(self):
        if not self.cart:
            print("🛒 Your cart is empty. Nothing to checkout.")
            return
        total = 0
        print(f"\n🧾 Order Summary for {self.name}")
        for item, qty in self.cart:
            if item.stock >= qty:
                item.update_stock(qty)
                amount = item.price * qty
                print(f"{item.name} x {qty} = ₹{amount}")
                total += amount
            else:
                print(f"❌ Not enough stock for {item.name}")
        print(f"💰 Total Bill: ₹{total}")
        self.cart.clear()

    def show_menu(self, admin):
        print(f"\n👤 Customer: {self.name}")
        while True:
            print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                admin.show_products()
            elif choice == '2':
                pid = int(input("Enter Product ID: "))
                found = False
                for product in admin.products:
                    if product.pid == pid:
                        qty = int(input("Enter quantity: "))
                        self.add_to_cart(product, qty)
                        found = True
                        break
                if not found:
                    print("❌ Product not found.")
            elif choice == '3':
                self.view_cart()
            elif choice == '4':
                self.checkout()
            elif choice == '5':
                break
            else:
                print("❌ Invalid choice")

# -----------------------------
# Main Execution
# -----------------------------
def main():
    print("🛍️ Welcome to Mini E-Commerce System")
    admin = Admin("AdminUser")
    
    # Preloaded products (optional)
    admin.add_product(Product(101, "Laptop", 50000, 10))
    admin.add_product(Product(102, "Phone", 20000, 15))
    admin.add_product(Product(103, "Headphones", 2000, 20))

    while True:
        print("\nLogin as:\n1. Admin\n2. Customer\n3. Exit")
        user_type = input("Enter choice: ")
        if user_type == '1':
            admin.show_menu()
        elif user_type == '2':
            name = input("Enter your name: ")
            customer = Customer(name)
            customer.show_menu(admin)
        elif user_type == '3':
            print("👋 Thank you for using the system!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
