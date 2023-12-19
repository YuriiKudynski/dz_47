import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, mode='r') as csv_file_reader:
            csv_read = csv.DictReader(csv_file_reader)
            lst = list(csv_read)
            dict_file = {}
            for i, data in enumerate(lst):
                dict_file[i + 1] = data

        with open('output_table.json', mode='w') as json_file:
            json.dump(dict_file, json_file, indent=4)
        return f'Успішна конвертація'
    except Exception as e:
        return f'Не успішна конвертація!{e}'


csv_f = 'input_table.csv'
result = convert_csv_to_json(csv_f)
print(result)
