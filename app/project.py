import csv
from collections import namedtuple

Task = namedtuple("Task", ["title", "duration", "prerequisites"])

def read_tasks(planner):
    tasks = {}
    for row in csv.reader(open(planner, encoding='utf-8-sig')):
        number = int(row[0])
        title = row[1]
        duration = float(row[2])
        prerequisites = set(map(int, row[3].split()))
        tasks[number] = (title, duration, prerequisites)

    return tasks

tasks = read_tasks("../resources/planner.csv")

print("To run the application, type 'tasks'.")
