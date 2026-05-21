from time import sleep

tasks = []

def show_tasks():
    count = 0
    if len(tasks) == 0:print("You have no tasks yet\n");sleep(0.5)
    for task in tasks:
        count += 1
        print(f"{count}: {task}");sleep(1)

def add_task():
    Addtask = input("Add a task: ");sleep(0.5)
    tasks.append(Addtask);print(f"Task Added {Addtask}\n");sleep(0.5)

def remove_tasks():
    count = 0
    for i in tasks:
        count += 1
        print(f"{count}: {i}")
    Removetasks = int(input("Remove a task: \n"));sleep(0.5)
    Removetasks -= 1
    tasks.pop(Removetasks)

while True:
    user = input("-----TO DO LIST -----\n1()Add Task\n2()View Tasks\n3()Remove Tasks\n");sleep(0.5)
    
    match user:
        case "1": add_task()
        case "2": show_tasks()
        case "3": remove_tasks()
        case "4": print("Goodbye"); exit()
