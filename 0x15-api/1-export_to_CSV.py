#!/usr/bin/python3
"""
Extend your Python script to export data in the CSV format
"""
import csv
import requests
import sys
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
    with open("{}.csv".format(emp_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_dict:
            taskwriter.writerow([int(emp_id), emp_info.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
