#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

from requests import get
import json

if __name__ == "__main__":
    # Get the todos data
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    # Get the users data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    # Create a dictionary to store the tasks for each user
    todo_all_employees = {}

    # Iterate over the users
    for user in data2:
        user_id = user['id']
        user_tasks = []

        # Iterate over the tasks
        for task in data:
            # Check if the task belongs to the current user
            if task['userId'] == user_id:
                # Create a new dictionary for the task
                task_dict = {
                    'username': user['username'],
                    'task': task['title'],
                    'completed': task['completed']
                }
                user_tasks.append(task_dict)

        # Add the tasks to the dictionary, using the user ID as the key
        todo_all_employees[user_id] = user_tasks

    # Write the dictionary to a JSON file
    with open("todo_all_employees.json", "w") as f:
        json.dump(todo_all_employees, f)
