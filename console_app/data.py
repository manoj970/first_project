from datetime import datetime
from array import array
from console_app.stock_update import *

class Inventory:
    
    REORDER_LEVEL = 25
    MINIMUM_STOCK_LEVEL = 50

    def __init__(self,product_name , category , sku  , supplier_credentials , warehouse_location):
        self.product_name = product_name
        self.category = category
        self.sku = sku
        self.supplier_credentials = supplier_credentials
        self.warehouse_locations = warehouse_location

        self.product_details = {
            "name": product_name,
            "category": category,
            "sku": sku,
            "current_stock": 100,
            "unit_price": 3499.0
        }
        self.user_operation_log = []

        self.supplier_credentials = supplier_credentials

        self.warehouse_locations = warehouse_location

        self.inventory_transaction_history_array = array("i", [1000, -200, 500, -300, 400])
        self.inventory_transaction_history = [
            (1000.0, datetime(2024, 6, 1, 10, 0)),
            (-200.0, datetime(2024, 6, 2, 14, 30)),
            (500.0, datetime(2024, 6, 3, 9, 15)),
            (-300.0, datetime(2024, 6, 4, 16, 45)),
            (400.0, datetime(2024, 6, 5, 11, 20))
        ]
    def verify_supplier(self, pin):
        try:
                pin = input("Enter Supplier PIN: ")
                if pin in self.supplier_credentials:
                    print("Supplier Verified")
                    self.user_operation_log.append("Supplier Verified")
                else:
                    print("Invalid Supplier PIN")
                    self.user_operation_log.append("Invalid Supplier Attempt")
        except Exception as e:
            print(f"the error was caught: {e}")        
        finally:
            print("Supplier verification attempted.")    

    def view_transactions(self):
        try:
            if not self.inventory_transaction_history:
                print("No transactions available.")
                return

            print("Recent Transactions:")
            for record in transaction_generator(self.inventory_transaction_history):
                print(record)
            self.user_operation_log.append("Viewed Transactions")
        except Exception as e:
            print(f"the error was caught: {e}")
        finally:
            print("View transactions attempted.")  
class InvalidDateError(Exception):
    pass
def display_info(self):
    print("=============== Product Details=============")
    try:
        for key,value in self.product_details.items():
            print(f"{key.capitalize()}: {value}")
            print(f"Reorder level is: {Inventory.REORDER_LEVEL} ")
            print(f"Minimum stock level is : {Inventory.MINIMUM_STOCK_LEVEL}")
    except Exception as e:
        print("Error caught: " , e)        



    





 


