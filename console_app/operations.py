from console_app.data import *
from console_app.stock_update import *
from datetime import datetime

class operation:

    def apply_discount(self):
        try:
            percent = get_valid_float("Enter discount percentage: ")

            original_price = product_details["unit_price"]
            product_details["unit_price"] = calculate_discount(original_price, percent)

            user_operation_log.append(f"Discount applied: {percent}%")
            print(f"Price changed from {original_price} to {product_details['unit_price']}")
        except Exception as e:
            print(f"the error was caught: {e}")    
        finally:
            print("Apply discount attempted.")    


    def check_reorder(self):
        try:
            stock = product_details["current_stock"]
            if stock <= REORDER_LEVEL and stock > 0:
                print("Low Stock - Reorder Needed")
            elif stock == 0:
                print("Out of Stock")
            else:
                print("Stock level is sufficient")

            user_operation_log.append("Checked Reorder Status")
        except Exception as e:
            print(f"the error was caught: {e}")
        finally:
            print("Check reorder status attempted.")        

    def total_inventory_value(self):
        try:
            total_value = product_details["current_stock"] * product_details["unit_price"]
            print("Total Inventory Value:", total_value)
            user_operation_log.append("Viewed Total Inventory Value")
        except Exception as e:
            print(f"the error was caught: {e}")
        finally:
            print("View total inventory value attempted.") 
            

    def transaction_filter(start_date, end_date):
        global inventory_transaction_history
        print(f"Filtering transactions from {start_date} to {end_date}")
        try:
            for stock , timestamp in inventory_transaction_history:
                if start_date <= timestamp <= end_date:
                    print(f"Stock change: {stock}, Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    raise InvalidDateError(f"Transaction date is invalid")    
        except InvalidDateError as e:
            print(f"the invalid date error was caught: {e}")           
        except Exception as e:
            print(f"the error was caught: {e}")     
        finally:
            print("Transaction filter attempted.")         




   
                