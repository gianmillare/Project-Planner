import csv
import tkinter
from collections import namedtuple
from tkinter.filedialog import askopenfilename

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



def draw_chart(tasks, canvas, row_height=40, title_width=300,
               line_height=40, day_width=20, bar_height=20,
               title_indent=20, font_size=-16):

    # define height and width
    height = canvas["height"]
    width = canvas["width"]

    week_width = 5 * day_width

    # create a line to separate the header from the rest of the applciation
    canvas.create_line(0, row_height, width, line_height, fill="gray")

    # Begin the loop for the application:
    for week_number in range(5):
        x = title_width + week_number * week_width

        # Draw a vertical line to separate x from the rest of the application
        canvas.create_line(x, 0, x, height, fill="gray")
        
        # include the text
        canvas.create_text(x + week_width / 2, row_height / 2,
                           text=f"Week {week_number+1}",
                           font=("Helvetica", font_size, "bold"))

        start_days = order_tasks(tasks)
        y=row_height
        for task_number in start_days:
            task = tasks[task_number]
               
def open_project():
    filename = askopenfilename(title="Open project", initialdir=".", filetypes=[("CSV Document", "*.csv")])

    tasks=read_tasks("../resources/planner.csv")
    draw_chart(tasks, canvas)

# Initial code to call tkinter and open the "tk" window
root = tkinter.Tk()

# Give the window a title
root.title("Project Planner")

# Create a button widget
open_button = tkinter.Button(root, text="Open Project...", command=open_project)
open_button.pack(side="top")

# Create a Canvas
canvas = tkinter.Canvas(root, width=800, height=400, bg="white")
canvas.pack(side="bottom")

# Main function of tkinter for event-handling
tkinter.mainloop()
