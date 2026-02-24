from console_app.data import *
print(f"the inventory  history  is: {inventory_transaction_history_array}\n")
debit_stock = [stock for stock in inventory_transaction_history_array if stock < 0]
print(f"the debit stocks are:{debit_stock}\n")
credit_stock = [stock for stock in inventory_transaction_history_array if stock >0]  
print(f"the reordered stocks are:{credit_stock}\n")   