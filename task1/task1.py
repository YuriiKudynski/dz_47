import json
import pickle

strng = """{
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": 34,
        "salary": 54000
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": 24,
        "salary": 40000
    }
}"""

data = json.loads(strng)
print("Тип обєкта: ", type(data))
print(data)

data["emp3"] = {"name": "Andrew", "designation": "Trainee", "age": 28, "salary": 30000}

# Серіалізація за допомогою dump у файл json
with open("data_j.json", 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Серіалізація за допомогою модуля pickle у бінарний файл
with open("data_p.pkl", 'wb') as pickle_file:
    pickle.dump(data, pickle_file)

# Десеріалізація з файлу json
with open("data_j.json", 'r') as json_file:
    des_json_data = json.load(json_file)

# Десеріалізація з pickle
with open("data_p.pkl", 'rb') as pickle_file:
    des_pickle_data = pickle.load(pickle_file)

print("json == pickle:", des_json_data == des_pickle_data)
print("json is pickle:", des_json_data is des_pickle_data)
