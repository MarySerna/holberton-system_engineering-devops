#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format
"""

import sys
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
    Completes request with provided info
    """
    url = "https://jsonplaceholder.typicode.com"
    emp_id = sys.argv[1]
    emp_info = requests.get("{}/users/{}".format(url, emp_id)).json()
    todo_dict = requests.get("{}/todos?userId={}".format
                             (url, emp_id)).json()
    empname = emp_info.get("name")
    tasks = []
    for task in todo_dict:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = empname
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[emp_id] = tasks
    with open("{}.json".format(emp_id), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
