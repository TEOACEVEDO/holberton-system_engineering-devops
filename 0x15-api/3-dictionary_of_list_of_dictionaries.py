#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
from asyncio import tasks
import requests
import json


if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/"

    all_users = requests.get(users_url).json()
    new_json = {}
    for i in all_users:
        tasks = requests.get(todos_url, params={"userId": i.get("id")}).json()

        list = []
        for tt in tasks:
            array = {}
            array['task'] = tt.get("title")
            array['completed'] = tt.get("completed")
            array['username'] = tt.get("username")
            list.append(array)
        new_json[i.get("id")] = list

        with open('todo_all_employees.json', 'w') as outfile:
            json.dump(new_json, outfile)
