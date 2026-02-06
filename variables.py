#  Create variables for name, age, height and print them in one sentence
user_name = "manoj"
_age = 21
_height = 172
print(f'User Name: {user_name}, Age: {_age}, Height: {_height}')

# Write code to calculate and print area of rectangle (length × width).
length = 5
width = 3
area_of_rectangle = length * width
print(f'Area of Rectangle: {area_of_rectangle}')

# Ask user for two numbers and print their sum, difference, product.
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
sum_of_numbers = first_number + second_number
difference_of_numbers = first_number - second_number
product_of_numbers = first_number * second_number
print(f'Sum: {sum_of_numbers}, Difference: {difference_of_numbers}, Product: {product_of_numbers}')

# Create variables price and tax_rate, calculate final price with tax.
price = 100
tax_rate = 0.18
final_price = price + (price * tax_rate)
print("Final price with tax: " ,final_price)

# Swap values of two variables without using a third variable.
first_name = "manoj"
last_name = "merugu"
first_name,last_name = last_name,first_name
print(f'First Name: {first_name}, Last Name: {last_name}')

# Convert temperature from Celsius to Fahrenheit (F = C × 9/5 + 32).
celcius = 20
fahrenheit = (celcius * 9/5) + 32
print(f'Temperature in Fahrenheit: {fahrenheit}')

# Calculate simple interest: principal × rate × time / 100.
principal = 100000
rate = 1.5
time = 12
simple_intrest = (principal * rate * time) / 100
print(f'Simple Interest: {simple_intrest}')

# Take user input for radius and calculate circle area (pi ≈ 3.14).
radius = int(input("Enter the radius of the circle: "))
PI = 3.14
area_of_circle = PI * (radius ** 2)
print(f'Area of Circle: {area_of_circle}')

# Create variables for hours and rate, calculate weekly pay.
hours = 40
rate = 15
weekly_pay = hours * rate
print(f'Weekly Pay: {weekly_pay}')

# Ask user for three numbers and print the largest one.
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))
largest_number = first_number
if second_number > largest_number:
    largest_number = second_number
if third_number > largest_number:
    largest_number = third_number
print(f'Largest Number: {largest_number}')