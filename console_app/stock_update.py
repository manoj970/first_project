from console_app.data import *
from console_app.util import *
from console_app.decorator import *
from console_app.stock_history import *
from datetime import datetime
@log_operation("stock update")
def update_stock():
 stock_change = get_valid_integer("Enter stock change (+add / -deduct): ")
 try:
        previous_stock = product_details["current_stock"]
        product_details["current_stock"] += stock_change


        if product_details["current_stock"] < 0:
            product_details["current_stock"] = 0
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        inventory_transaction_history.append((stock_change,current_time))
        print(f"the updated transaction history is: {inventory_transaction_history}\n")
        user_operation_log.append(f"[{current_time}]Stock changed by {stock_change}")

        print(f"[{current_time}]Stock updated from {previous_stock} to {product_details['current_stock']}")
        log_stock_history( action = f"Stock updated from {previous_stock} to {product_details['current_stock']}", stock = stock_change)
    
 except TypeError as e:
         print(f"the type error was caught: {e}")    
 except ValueError as e:
        print(f"the value error was caught: {e}")
 except NameError as e:
        print(f"the name error was caught: {e}")        
 except Exception as e:
        print(f"the error occured : {e}") 
 finally:
        print("Stock update operation attempted.")    

      
