# # Create variables of each main type (int, float, str, bool, list, dict) and print their types.
int = 1
float = 1.1
str = "Hello, World!"
bool = True
list = [1, 2, 3, 4, 5]
dict = {"name": "Manoj", "age": 21, "city": "Mancherial"}
print (f'Integer: {int}, Type: {type(int)}')
print (f'Float: {float}, Type: {type(float)}')
print (f'String: {str}, Type: {type(str)}')
print (f'Boolean: {bool}, Type: {type(bool)}')  
print (f'List: {list}, Type: {type(list)}')
print (f'Dictionary: {dict}, Type: {type(dict)}')

# Take user input for name and age, print "Hello [name], you are [age] years old."
name = input("Enter the name: ")
age = input("Enter the age: ")
print(f'Hello {name} , you are {age} years old. ')

# Calculate and print area of rectangle using length and width (float).
length = 2.5
width = 3.5
area_of_rectangle = length * width
print(f'Area of Rectangle: {area_of_rectangle}')

# Create a list of 5 products and print the second one.
products_list = ["Laptop", "Smartphone", "Headphones", "Powerbank", "Smartwatch"]
print(products_list[1])

# Make a dictionary for a user with name, age, city, and print it.
user_info = {"user_name": "Manoj",
              "age": 21,
                "city": "Mancherial"}
print(user_info)

# Convert string "123.45" to float and add 10 to it.
string_number = "123.45"
float_number = float(string_number)
result = float_number + 10
print(f'Result: {result}')

# Check if a number is positive, negative, or zero (use bool).
number = int(input("Enter a number: "))
if number ==0:
    print(" zero.")
else:     
 result = number > 0

 print(result)

#  Create a tuple of 4 colors and try to change one (see the error).
colors = ("Red", "Green", "Blue", "Yellow")
# colors[1] = "Purple"  # TypeError: 'tuple' object does not support item assignment

# Make a set from list [1,2,2,3,3] and print it.
list = [1, 2, 2, 3, 3]
set = set(list)
print(set)







