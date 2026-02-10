# ================================TO-DO'S=================================================
# Write a function to add two numbers and return the sum.
def add(a , b):
    result = a+b
    return result
print(add(4 , 5))
# Create a function that takes name and prints "Hello, name!".
def greet(name , wish):
    print(f"{wish} , {name} !")
greet(name = "manoj" ,wish ="Hello")    
# Write a function to calculate area of rectangle (length × width).
def area_of_rectangle(length , width):
    area = length * width
    return area
print(area_of_rectangle(length = 4 , width = 6))
# Make a function that checks if number is even or odd.
def number_check():
    number =int(input("Enter the number: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
number_check()        
# Create function to find maximum of three numbers.
def largest_number(number_01, number_02, number_03):
    if number_01 > number_02 and number_03:
        return number_01
    elif number_02 > number_01:
           return number_02
    else:
        return number_03
print(f"the largest number is: ",largest_number(12,54,7))       

# Write function that takes list of prices and returns total.
def total_amount():
    prices = [123 ,234 ,3424 , 6564 ]
    total = sum(prices)
    return total
print(f"sum of all prices is :",total_amount())
# Make greeting function with default name="Guest".
def greeting(name = "Guest" , wish = "Welcome"):
    print(f"{wish} {name} Good to see you")
greeting(name = "manoj")    
# Function to check if size is in available sizes list.
def check_size():
    customer_size = input("Enter the customer size: ")
    available_sizes = ['M' ,'L' ,'XL' ,'XXL' ]
    if customer_size in available_sizes:
        print(f"customer size is available: ",customer_size ,available_sizes)
    else:
        print("the customer size is not available")    
check_size()
# Create function to format price with ₹ symbol and 2 decimals.
def format_price(price):
    print( f"${price: .2f}")
format_price(2323)    
# Write function that takes **kwargs and prints user profile.