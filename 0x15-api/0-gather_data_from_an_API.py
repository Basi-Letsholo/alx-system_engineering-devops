#!/usr/bin/python3
"""Script to gather data from an API."""


import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <EMPLOYEE ID>")
        sys.exit(1)

    emp_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user_response = requests.get(user_url).json()
    name = user_response.get("name")

    todo_url = f"https://jsonplaceholder.typicode.com/todos/{emp_id}"
    todo_data = requests.get(todo_url).json()

    done_url = f"https://jsonplaceholder.typicode.com/todos?userID={emp_id}&completed=true"
    done_data = requests.get(done_url).json()
    len_done = len(done_data)

    not_done_url = f"https://jsonplaceholder.typicode.com/todos?userID={emp_id}&completed=false"
    not_data = requests.get(not_done_url).json()
    len_not = len(not_data)

    print(f"Employee {name} is done with tasks({len_done}/{len_not}):")
    for task in done_data:
        print("\t "+task.get('title'))
