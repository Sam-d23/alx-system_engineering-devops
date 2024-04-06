#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # API URL
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user information
    user_response = requests.get(base_url + "users/{}".format(sys.argv[1]))
    user_data = user_response.json()
    
    # Fetch TODO list for the employee
    todos_response = requests.get(base_url + "todos", params={"userId": sys.argv[1]})
    todos_data = todos_response.json()

    # Extract completed task titles
    completed_titles = [task.get("title") for task in todos_data if task.get("completed")]

    # Print employee TODO progress
    print("Employee {} is done with tasks ({}/{}):".format(
        user_data.get("name"), len(completed_titles), len(todos_data)))
    for title in completed_titles:
        print("\t", title)
