import csv

def read_tasks(project_planner):
    tasks = {}
    for row in csv.reader(open(project_planner)):
        number = row[0]
        title = row[1]
        duration = row[2]
        prerequisites = row[3]
        tasks[number] = (title, duration, prerequisites)

    return tasks

tasks = read_tasks("../resources/planner.csv")

print("To run the application, type 'execute'.")
