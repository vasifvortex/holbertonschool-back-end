#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_tasks = requests.get(
            'https://jsonplaceholder.typicode.com/users/' +
            f'{sys.argv[1]}/todos'
        )
        user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            f'{sys.argv[1]}')

        user_tasks = json.loads(user_tasks.text)
        user = json.loads(user.text)
        user_name = user["username"]
        task_list = []
        for task in user_tasks:
            task_dict = {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_name
            }
            task_list.append(task_dict)

        with open(f'{sys.argv[1]}.json', "w") as file:
            record = {}
            record[sys.argv[1]] = task_list
            json.dump(record, file)
