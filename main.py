import json
try:
    filename="statistics.json"
    with open (filename,'r') as file:
        data=json.load(file)

