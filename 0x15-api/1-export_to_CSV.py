#!/usr/bin/python3
"""
Python script that exports data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    # Send a GET request to retrieve TODO list data
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    # Initialize an empty row list
    row = []

    # Send a GET request to retrieve user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    # Find the employee username based on the provided ID
    for i in data2:
        if i['id'] == int(argv[1]):
            employee = i['username']

    # Create a CSV file with the employee ID as the file name
    with open(argv[1] + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Iterate over the TODO list data
        for i in data:
            row = []
            if i['userId'] == int(argv[1]):
                # Append the required fields to the row list
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                # Write the row to the CSV file
                writer.writerow(row)
