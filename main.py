
from console_app.data import *
from console_app.decorator import *
from console_app.util import *
from console_app.operations import *
from console_app.display import *
from console_app.stock_update import *
from datetime import datetime
def main():
    print("====== Product Inventory System ======")
    display_product()

    while True:
        action = input("""choose an action:
                       1. Update Stock
                       2. View Transactions
                       3. Verify Supplier
                       4. Apply Discount
                       5. Check Reorder Status
                       6. View Total Inventory Value
                       0. Exit
                       Enter your choice: """)

        if action == "1":
            update_stock()
        elif action == "2":
            view_transactions()
        elif action == "3":
            verify_supplier()
        elif action == "4":
            apply_discount()
        elif action == "5":
            check_reorder()
        elif action == "6":
            total_inventory_value()   
        elif action == "0":
            break
        else:
            print("Invalid option. Please select a valid choice.")

    print("\nFinal Product Details:")
    display_product()
    display_user_operations()
    # list comphrehension
    print (f"the transaction history is: {inventory_transaction_history}\n")
    debit_trans = [(stock,timestamp) for stock, timestamp in inventory_transaction_history if stock < 0]
    print(f"the debit transactions are:{debit_trans}\n")

    # set comphrehensions

    new_location = "Hyderabad"
    warehouse_location = {location for location in warehouse_locations if location != new_location}| {new_location}
    print(f"the warehouse locations are: {warehouse_location}\n")
    # dictionary comphrehensions
    print(inventory_transaction_history)
    transaction_summary = {stock :timestamp for stock ,timestamp in inventory_transaction_history}
    print("=================================================\n")
    print(transaction_summary)

    # transaction filteration
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")          
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    transaction_filter(start_date, end_date)



if __name__ == "__main__":
    main()
