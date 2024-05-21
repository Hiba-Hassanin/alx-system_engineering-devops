#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    # Send a GET request to retrieve TODO list data
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    # Initialize variables for counting completed tasks and total tasks
    completed = 0
    total = 0

    # Initialize a list to store task titles
    tasks = []

    # Send a GET request to retrieve user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    # Find the employee name based on the provided ID
    for i in data2:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    # Iterate over the TODO list data
    for i in data:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    # Print the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee, completed, total))

    for i in tasks:
        print("\t {}".format(i))
