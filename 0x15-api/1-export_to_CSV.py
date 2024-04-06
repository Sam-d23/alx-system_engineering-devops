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

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(base_url + "users/{}".format(user_id))
    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(base_url + "todos", params={"userId": user_id})
    todos_data = todos_response.json()

    # Write to CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write header row
        writer.writerow(["User ID", "Username", "Completed", "Title"])
        # Write todo items
        for todo in todos_data:
            writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])
