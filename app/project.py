import csv

encoding='utf-8-sig'

def read_tasks(planner):
    tasks = {}
    for row in csv.reader(open(planner, encoding='utf-8-sig')):
        number = row[0]
        title = row[1]
        duration = row[2]
        prerequisites = row[3]
        tasks[number] = (title, duration, prerequisites)

    return tasks

tasks = read_tasks("../resources/planner.csv")

print("To run the application, type 'tasks'.")
