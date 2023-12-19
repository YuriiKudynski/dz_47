import json


def validate_json(data):
    try:
        des_data = json.loads(data)
        print("Valid JSON")
    except json.JSONDecodeError as e:
        print(f"Invaild JSON: {e}")


with open('data_j_inv.json', mode='r') as file:
    json_data = file.read()

with open('data_j.json', mode='r') as file2:
    json_data_valid = file2.read()

validate_json(json_data)
validate_json(json_data_valid)
