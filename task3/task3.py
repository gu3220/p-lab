import json

path_values, path_tests, path_report = input().split()

with open(path_values) as file:
    load_values = json.load(file)
with open(path_tests) as file:
    load_tests = json.load(file)

save_values = {}
for value in load_values['values']:
    save_values.update({value['id'] : value['value']})

def get_results(test):
    for item in test:
        if ('value' in item):
            item['value'] = save_values[item['id']]
        if ('values' in item):
            get_results(item['values'])
    return

get_results(load_tests['tests'])

with open(path_report, 'w') as file:
    json.dump(load_tests, file, indent=2)
