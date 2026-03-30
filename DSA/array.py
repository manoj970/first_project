# Create a list of 5 products and print them with numbers (1. Shirt, 2. Cap…).
products = ["Shirt", "Cap", "Shoes", "Jeans", "Jacket"]

for i in range(len(products)):
    print(f"{i+1}. {products[i]}")
# Add "watch" to the end and "tie" to the beginning of the list.
products.append("watch")
products.insert(0, "tie")
print (products)
# Remove the second item and print the updated list.
products.remove(products[1])
print (products)

# Check if "shoes" is in the list and print "Available" or "Not found".
if "Shoes"  in products:
        print("Available")
else:
        print("Not found")
    
# Reverse the list and print it.
products.reverse()
print(products)
# Sort a list of prices [1200, 800, 1500, 999] in ascending order.
list = [1200, 800, 1500, 999]
list.sort()
print(list)

# Count how many times "shirt" appears in the list.
print(products.count("Cap"))
# Create a list from user input (ask 3 times and append).
list=[]
for item in range(3):
       item = int(input("Enter the number: "))
       list.append(item)
print(list)       
# Make a copy of the list and add a new item to the copy only.
a = [1,3,2]
b = a.copy()
b.append(4)
print(a)
print(b)
# Print only items that start with "B" (use loop).
for element in products:
       if element.startswith("J"):
              print(element)