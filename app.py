tasks = []

def create_task(title):
    task = {
        "title": title,
        "status": "todo"
    }
    tasks.append(task)

create_task("Study Git")
print(tasks)

def list_tasks():
    for task in tasks:
        print(task)

list_tasks()