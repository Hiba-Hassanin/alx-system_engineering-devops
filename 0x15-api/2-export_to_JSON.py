#!/usr/bin/python3
"""
Python script that exports data in the JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    # Send a GET request to retrieve TODO list data
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    # Initialize variables
    row = []

    # Send a GET request to retrieve user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    # Find the employee username and ID based on the provided ID
    for i in data2:
        if i['id'] == int(argv[1]):
            u_name = i['username']
            id_no = i['id']

    # Iterate over the TODO list data
    for i in data:
        new_dict = {}

        # Check if the task belongs to the provided employee ID
        if i['userId'] == int(argv[1]):
            new_dict['username'] = u_name
            new_dict['task'] = i['title']
            new_dict['completed'] = i['completed']
            row.append(new_dict)

    # Create a dictionary with the employee ID as the key
    final_dict = {}
    final_dict[id_no] = row

    # Convert the dictionary to a JSON object
    json_obj = json.dumps(final_dict)

    # Create a JSON file with the employee ID as the file name
    with open(argv[1] + ".json", "w") as f:
        f.write(json_obj)
