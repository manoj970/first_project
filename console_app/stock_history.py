import json
from datetime import datetime
def log_stock_history(action , stock = None):
    log_entry ={
            "timestamp ": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action" : action,
            "stock" : stock
        }
    try:
        with open("stock_history.json", "a") as file:
            json.dump(log_entry , file)
            file.write("\n")  
            print("transaction log added successfully.") 
    except Exception as e:        
        print(f"Error caught: {e}")
    
