from console_app.operations import *
def display_product():
    print("========== PRODUCT DETAILS ==========")
    try:
        for key, value in product_details.items():
            print(f"{key} : {value}")
        print("=====================================")
    except Exception as e:
        print (f"the error was caught: {e}")   
    finally:
        print("display product attempted.")    

    
def display_user_operations():
    print("========== USER OPERATIONS ==========")
    try:

        if not user_operation_log:
            print("No operations performed.")
        else:
            for index, operation in enumerate(user_operation_log, 1):
                print(f"{index}. {operation}")

        print("=====================================")
    except Exception as e:
        print(f" the error was caught: {e}")   
    finally:
        print(" user operations attempted.") 
