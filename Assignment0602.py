# =================================TO DO'S=========================================


## USE CASE: ProductApp - Inventory & Data Structure Management

# This application demonstrates variable usage and data structures in a product management system.

# ## Key Features:
# 1. Product Information Management: Store product details using dictionaries
# 2. Inventory History: Maintain list of all stock transactions
# 3. Security Credentials: Store multiple supplier PINs using tuples
# 4. Warehouse Locations: Track product locations using sets
# 5. Stock Operations: Add/deduct inventory and calculate reorder points
# 6. Alert System: Apply alerts for low stock

# ## Data Structures Used:
# - inventory_history (List): [100, 50, 75, 120, 45] - mutable, ordered stock changes
# - supplier_cred (Tuple): ("SUP123","SUP456") - immutable, secure supplier IDs
# - warehouse_locations (Set): {"warehouse_A", "warehouse_B", "warehouse_C"} - unique locations
# - product_info (Dictionary): {name, category, sku, current_stock} - key-value mappings

# ## Flow:
# 1. Initialize product with lists, tuples, sets, and dictionaries
# 2. Display inventory history
# 3. Add/deduct stock transactions and update inventory
# 4. Manage supplier credentials and warehouse locations
# 5. Calculate reorder levels based on stock trends
# 6. Check and apply alerts if stock below threshold
# 7. Display final product information with updated data

# Initialize the variables
product_name = "Tablet"
product_category = "electronics"
sku = "NO660"
current_stock = 50
MINIMUM_STOCK_LEVEL = 10
REORDER_THRESHOLD = 20
is_active = True
wallet_balance = 10000.00
inventory_history = [9000, 7000 , -6500 ,4500 , 3500]
supplier_cred = ("SUP123","SUP456")
warehouse_locations = {"warehouse_A", "warehouse_B", "warehouse_C", "warehouse_D"}
product_details = {
                    "Product Name": {product_name},
                    "Category": {product_category},
                    "Sku": {sku},
                    "current_stock": {current_stock},
                    "Minimum Stock level ": {MINIMUM_STOCK_LEVEL},
                    "Reoreder threshold": {REORDER_THRESHOLD},
                    "Is Active": {is_active},
        
    }
print("================================ Initial Product Details ===============================")
print(f"Product_DEtails: {product_details}")

def inventory_transactions(new_transaction):
    global wallet_balance , inventory_history
    print("================================ Inventory History ===============================")
    print(f"Stock Transactions beforing adding: {inventory_history}")
    print(f"Current Wallet Balance: {wallet_balance}")
    inventory_history.append(new_transaction)
    wallet_balance += new_transaction 
    print(f"Stock Transactions after adding: {inventory_history}")
    print(f"Updated Wallet Balance: {wallet_balance}")

def add_stock(new_stock):
    global current_stock
    print("================================ Stock Update ===============================")
    print(f"Current Stock before addition: {current_stock}")
    current_stock += new_stock
    print(f"Current Stock after addition: {current_stock}")

def deduct_stock(stock_to_deduct):
    global current_stock
    print("================================ Stock Deduction ===============================")
    print(f"Current Stock before deduction: {current_stock}")
   
    if stock_to_deduct > current_stock:
            print("⚠️ Warning: Not enough stock to deduct.")
    else:
        current_stock -= stock_to_deduct
        print(f"Current Stock after deduction: {current_stock}")
def manage_supplier_credentials(new_cred):
    global supplier_cred
    print("================================ Supplier Credentials ===============================")
    print(f"Current Supplier Credentials: {supplier_cred}")
    supplier_cred += (new_cred,)
    print(f"Updated Supplier Credentials: {supplier_cred}")

def manage_warehouse_locations(new_location):
    global warehouse_locations
    print("================================ Warehouse Locations ===============================")
    print(f"Current Warehouse Locations: {warehouse_locations}")
    warehouse_locations.add(new_location)
    print(f"Updated Warehouse Locations: {warehouse_locations}")

def alert_system():
    global current_stock, REORDER_THRESHOLD, MINIMUM_STOCK_LEVEL
    print("================================ Alert System ===============================")
    if current_stock <= REORDER_THRESHOLD:
        print(" ⚠️⚠️ Alert: Stock is low, reorder the product.")
        print(" Reorder the product soon to avoid stockouts.")
        if current_stock <= MINIMUM_STOCK_LEVEL:
            print(" ⚠️⚠️ Alert: Stock is at very low ,reorder immediately.")
    else:
        print(" Stock level is sufficient.")

def display_product_info():        
    print("================================ Final Product Info ===============================")
    print(f"product name: {product_name}")
    print(f"product category: {product_category}")
    print(f"product sku: {sku}")
    print(f"current stock: {current_stock}")
    print(f"wallet balance: {wallet_balance}")
    print(f"Location: {warehouse_locations}")
    print(f"Supplier Credentials: {supplier_cred}")

def main():
    inventory_transactions(2000)
    add_stock(100)
    deduct_stock(50)
    manage_supplier_credentials("SUP999")
    manage_warehouse_locations("warehouse_F")
    alert_system()
    display_product_info()
if __name__ == "__main__":
    main()    

           
    







