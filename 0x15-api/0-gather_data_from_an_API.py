#!/usr/bin/python3
"""Script to gather data from an API."""


import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <EMPLOYEE ID>")
        sys.exit(1)

    emp_id = sys.argv[1]

    base_url = f'https://jsonplaceholder.typicode.com/'

    users = f'users?id={emp_id}'
    todos = f'todos?userId={emp_id}'
    done = f'{todos}&completed=true'
    not_done = f'{todos}&completed=false'

    user_data = requests.get(f'{base_url}{users}').json()
    name = user_data[0].get("name")

    todo_data = requests.get(f'{base_url}{todos}').json()
    done_data = requests.get(f'{base_url}{done}').json()

    len_todo = len(todo_data)
    len_done = len(done_data)

    print(f'Employee {name} is done with tasks({len_done}/{len_todo}):')

    for task in done_data:
        print("\t "+task.get("title"))
