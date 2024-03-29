#!/usr/bin/python3
"""Script to gather data from an API."""


import json
import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <EMPLOYEE ID>")
        sys.exit(1)

    emp_id = sys.argv[1]

    base_url = f'https://jsonplaceholder.typicode.com/'

    users = f'users?id={emp_id}'
    todos = f'todos?userId={emp_id}'
    done = f'{todos}&completed=true'
    not_done = f'{todos}&completed=false'

    user_data = requests.get(f'{base_url}{users}').json()
    name = user_data[0].get("name")
    username = user_data[0].get("username")

    todo_data = requests.get(f'{base_url}{todos}').json()
    done_data = requests.get(f'{base_url}{done}').json()

    len_todo = len(todo_data)
    len_done = len(done_data)

    with open(f'{emp_id}.json', 'w') as json_file:
        data = {
                emp_id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username,
                    }
                    for task in todo_data
                    ]
                }
        json.dump(data, json_file)
