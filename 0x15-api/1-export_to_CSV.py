#!/usr/bin/python3
"""To-do list information for a given employee ID is exported to CSV."""

import csv
import requests
import sys


if __name__ == "__main__":
    #The user ID is gotten from the command-line arguments
    user_id = sys.argv[1]

    #The base URL for the JSON API is defined
    url = "https://jsonplaceholder.typicode.com/"

    #user information is fetched from the API and
    #The response is converted to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    #The username is extracted from the user data
    username = user.get("username")

    #the to-do list items associated with the given
    #user ID and convert the response to a JSON object are fetched
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # list comprehension is used to iterate over the to-do list items
    # Each item's details is written (user ID, username, completion status,
    #   and title) as a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
