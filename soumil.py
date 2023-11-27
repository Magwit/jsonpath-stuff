import json
from jsonpath_ng.ext import parse

with open("employee.json") as employee_json:
    employee_data = json.load(employee_json)

first_name_query = parse("$.first_name").find(employee_data)[0].value

print(first_name_query)
