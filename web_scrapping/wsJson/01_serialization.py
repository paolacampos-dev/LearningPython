import json

data = {
    "user":     {
        "name": "William Williams", 
        "age": 93
    }
}

# Serializat it (write py into Json) into a Json file
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

# to print it out 
json_str = json.dumps(data, indent=4)
print(json_str)  # {"user": {"name": "William Williams", "age": 93}}