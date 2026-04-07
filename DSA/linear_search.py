def linear_search(arr , name):
    for item in arr:
        if item ["name"] ==name:
            return f"name:{item["name"]} \n age:{item["age"]}  \n disease:{item["disease"]}"
arr =[
{"name": "Arjun", "age": 34, "disease": "Fever"},
{"name": "Meena", "age": 22, "disease": "Flu"},
{"name": "Ravi", "age": 45, "disease": "Diabetes"},
{"name": "Sneha", "age": 29, "disease": "Migraine"}
]
print(linear_search(arr , "Ravi"))