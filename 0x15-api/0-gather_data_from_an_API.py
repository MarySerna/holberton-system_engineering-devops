#!/usr/bin/python3
"""
Uses provided RESTful API to return employee todo progress info
"""
import requests
import sys


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
    completed = []
    for task in todo_dict:
        if task["completed"]:
            completed.append(task["title"])
    print("Employee {} is done with tasks({}/{}):".format(empname,
          len(completed), len(todo_dict)))
    for task in completed:
        print("\t {}".format(task))
