import json

# Python object (dictionary)
employee = {"name": "John Doe", "age": 30, "department": "Engineering"}

# Serialization
employee_json = json.dumps(employee, indent=4)
print("Serialized JSON:", employee_json)

# Deserialization
employee_dict = json.loads(employee_json)
print("Deserialized Dictionary:", employee_dict)

import random
def driving_license_vending_machine(event):
    print(f"function name: driving_license_vending_machine")
    age = event.get("age")
    name = event.get("name")
    if age >= 18:
        print(f"{name} is an Adult")

        dl_number = get_driving_license(name)
        return dl_number
    else:
        print(f"{name} is a Minor")
        return f"{name} is a minor DL cant be issued"
def get_driving_license(name):
    print("An adult is eligible to get a driving license")
    print(f"Driving license issued for {name}")
    dl_number = random.randint(100000, 999999)
    return dl_number

event = {
    "name": "John",
    "age": 12
}

return_value = driving_license_vending_machine(event=event)
print(return_value)
