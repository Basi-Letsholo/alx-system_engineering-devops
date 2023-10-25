#!/usr/bin/python3
"""Script to gather data from an API."""


import json
import requests
import sys

if __name__ == "__main__":

    emp_id = 1
    base_url = f'https://jsonplaceholder.typicode.com/'

    dict_data = {}

    while True:

        users = f'users?id={emp_id}'
        todos = f'todos?userId={emp_id}'
        done = f'{todos}&completed=true'
        not_done = f'{todos}&completed=false'

        user_data = requests.get(f'{base_url}{users}').json()

        if not user_data:
            break

        name = user_data[0].get("name")
        username = user_data[0].get("username")

        todo_data = requests.get(f'{base_url}{todos}').json()

        dict_data[emp_id] = [
                {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                for task in todo_data
            ]
        emp_id += 1

    with open(f'todo_all_employees.json', 'w') as dict_file:
        json.dump(dict_data, dict_file)
