#!/usr/bin/python3
"""Gather data from an API"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        res = requests.get('https://jsonplaceholder.typicode.com/users/' +
                           f'{sys.argv[1]}/todos')

        response_usr_todo = json.loads(res.text)
        todo_all_len = len(response_usr_todo)
        user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            f'{sys.argv[1]}')
        user_response = json.loads(user.text)
        user_name = user_response["username"]
        with open(f"{sys.argv[1]}.csv", "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
            for todo in response_usr_todo:
                csv_list = [str(todo['userId']), str(user_name),
                            str(todo['completed']), str(todo['title'])]
                writer.writerow(csv_list)
