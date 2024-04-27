#!/usr/bin/python3
import requests
import csv
import sys
import json


res = requests.get('https://jsonplaceholder.typicode.com/users/' +
                   f'{2}/todos')
response = json.loads(res.text)
print(res.json())
with open(f"2.csv","w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([["hey", "sa"],["hey"]])
    writer.writerow([["hey", "sa"],["hey"]])
# response = csv.loads(res.text)
# all_task = len(response)