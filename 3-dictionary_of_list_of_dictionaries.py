#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests


if __name__ == "__main__":
    record = {}
    for i in range(1, 11):
        user_tasks = requests.get(
            'https://jsonplaceholder.typicode.com/users/' +
            f'{i}/todos'
        )
        user = requests.get(
            'https://jsonplaceholder.typicode.com/users/' +
            f'{i}'
        )
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
        record[i] = task_list

    with open('todo_all_employees.json', "w") as file:
        json.dump(record, file)
