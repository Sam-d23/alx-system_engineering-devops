#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_response = requests.get(url + "users/{}".format(employee_id))
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch TODO list for the employee
    todos_response = requests.get(url + "todos",
                                  params={"userId": employee_id})
    todos_data = todos_response.json()

    # Write TODO list information to CSV file
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Employee ID", "Username", "Completed", "Title"])
        for todo in todos_data:
            writer.writerow([employee_id, username, todo["completed"],
                             todo["title"]])
