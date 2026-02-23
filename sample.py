file = open("sample.txt", "w")
file.write("hey, what's up?")
file.close()

file = open("sample.txt")
content = file.read()
print(content)
file.close()

file = open("sample.txt", "a")
file.write("\nI am learning file handling in Python.")
file.close()

file = open("2nd_sample.txt", "w")
file.write("This is the second sample file.")
file.close()

import os
os.remove("2nd_sample.txt")


from console_app.data import *
def stock_report(filename):
    global inventory_transaction_history
    try:
        with open(filename, 'w') as file:
            for stock, timestamp in inventory_transaction_history:
             file.write(f"{stock} : {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n") 
        print("Stock report generated successfully.")
    except Exception as e:
        print("the error was caught: ",e)   
stock_report("stock_report.txt")                 

import json
data = {
   "name" : "manoj",
    "age" : 21,
    "city" : "mancherial"
}
file = open("sample.json", "w")
json.dump(data , file)
file.close()