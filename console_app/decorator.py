def log_operation(operation):
    try:
        def decorator(func):
            
                def wrapper(*args, **kwargs):
                    print(f"{operation} started")
                    result = func(*args, **kwargs)
                    print(f"{operation} completed")
                    return result
                return wrapper
        return decorator
    except Exception as e:
         print(f"the error was caught: {e}")
    finally:
        print("Log operation attempted.")     
        


