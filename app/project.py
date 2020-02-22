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
        tasks[number] = Task(title, duration, prerequisites)
    
    return tasks

tasks = read_tasks("../resources/planner.csv")
tasks

def order_tasks(tasks):
    
    # Start the loop with all tasks marked as incomplete on day zero
    incomplete = set(tasks)
    completed = set()
    start_days = {}
    
    # Begin the while and for loops to loop through all incomplete tasks
    while incomplete:
        for task_number in incomplete:
            
            # check to make sure the prerequisites are completed for the task
            task = tasks[task_number]
            if task.prerequisites.issubset(completed):
                
                # Create a loop to identify the day the task can be started
                earliest_start_day = 0
                for prereq_number in task.prerequisites:
                    prereq_end_day = start_days[prereq_number] + tasks[prereq_number].duration
                    
                    # Once prereq is completed, the day the task is completed becomes the new earliest start day
                    if prereq_end_day > earliest_start_day:
                        earliest_start_day = prereq_end_day
                
                # Store the new earliest start day and mark the task as completed
                start_days[task_number] = earliest_start_day
                incomplete.remove(task_number)
                completed.add(task_number)
                break

    return start_days

