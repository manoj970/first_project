# =======================================TO- DO'S=========================================
## for Learners: Product-Oriented Application to get started with Variables
# USE CASE: ProductApp

# This application demonstrates variable usage in an e-commerce product management system.

# ## Key Features:
# 1. **Product Information**: Store product details (name, category, SKU)
# 2. **Inventory Tracking**: Monitor stock levels and quantities
# 3. **Low Stock Alert**: Notify when inventory falls below reorder threshold
# 4. **Product Status**: Track if product is active or discontinued

# ## Variables Used:
# - `application_name`: App identifier
# - `product_name`, `category`: Product identity
# - `sku`: Product code (unique identifier)
# - `supplier_id`: Supplier credential (numeric)
# - `current_stock`: Current inventory count
# - `MIN_STOCK_LEVEL`, `REORDER_THRESHOLD`: Stock thresholds (constants)
# - `is_active`: Product availability flag

# ## Program Flow:
# 1. Initialize product with default values
# 2. Validate product data (basic checks)
# 3. Display reorder threshold constant
# 4. Print all product information
# 5. Check inventory against alert threshold
# 6. Display product category and supplier details

# Initialize the variables
application_name = "ProductApp"
product_name = "smartphone"
product_catogory = "electronics"
_sku = "CN60"
supplier_id = 12345
current_stock = 30
is_active = True

# Constants for inventory management
MIN_STOCK_LEVEL = 10
REORDER_THRESHOLD = 20

# print all the product information
print("================================ Product Information ===============================")
print(f"Application Name: {application_name}")
print(f"Product Name: {product_name}")
print(f"SKU: {_sku}")
print(f"Supplier ID: {supplier_id}")
print(f"Current Stock: {current_stock}")
print(f"Is Active: {is_active}")
print(f"Minimum Stock Level: {MIN_STOCK_LEVEL}")
print(f"Reorder Threshold: {REORDER_THRESHOLD}")

# validate product data
if product_name == "":
 print("⚠️Warning: Product name cannot be empty.")
if supplier_id <= 0:
    print("⚠️Warning: Supplier ID is incorrectr.")
if current_stock < 0:
    print("⚠️Warning: Current stock cannot be negative.")
if _sku == "":
    print("⚠️Warning: SKU cannot be empty.")
if is_active :
   print("✅ Product is active and available.")
else:
    print("❌ Product is discontinued.")

print("""============BASIC CHECKS ARE DONE============""")

# check inventory against alert threshold
if current_stock <= REORDER_THRESHOLD:
            print("  Alert: Stock is low reorder the product.")
            print(" Reorder the product soon to avoid stockouts.")
if current_stock <= MIN_STOCK_LEVEL:
            print("  ⚠️Alert:stock is running critically low, immediate action required.")
if current_stock <=0:
            print(" product is out of stock")
else:
            print(" Stock level is sufficient.")        

# product category and supplier details
print(f"Product Category: {product_catogory}")
print(f"Supplier ID: {supplier_id}")



        




       





