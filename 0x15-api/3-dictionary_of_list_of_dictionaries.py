#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format
"""
import json
import requests


if __name__ == '__main__':
    employees = requests.get("https://jsonplaceholder.typicode.com/users",
                             verify=False).json()
    emp_dict = {}
    empname_dict = {}
    for user in employees:
        uid = user.get("id")
        emp_dict[uid] = []
        empname_dict[uid] = user.get("username")
    todo_dict = requests.get("https://jsonplaceholder.typicode.com/todos",
                             verify=False).json()
    for task in todo_dict:
        task_dict = {}
        uid = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = empname_dict.get(uid)
        emp_dict.get(uid).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(emp_dict, jsonfile)
