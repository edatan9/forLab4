tasks = {}

num_tasks = int(input("Enter number of tasks: "))

for i in range(num_tasks):
    task_name = input("Enter task name: ")
    dep_count = int(input(f"How many dependencies for {task_name}? "))

    dependencies = []
    for j in range(dep_count):
        dep_name = input(f"Enter dependency {j + 1}: ")
        dependencies.append(dep_name)

    tasks[task_name] = dependencies

print("TASK STRUCTURE:")
for task in tasks:
    print(f"{task} -> {tasks[task]}")

print("INITIAL TASKS (no dependencies):")
initial_tasks = []

for task in tasks:
    if len(tasks[task]) == 0:
        initial_tasks.append(task)

if len(initial_tasks) == 0:
    print("None")
else:
    for task in initial_tasks:
        print(task)

execution_order = []
completed = set()

while len(completed) < len(tasks):
    progress = False

    for task in tasks:
        if task not in completed:
            can_execute = True

            for dep in tasks[task]:
                if dep not in completed:
                    can_execute = False
                    break

            if can_execute:
                execution_order.append(task)
                completed.add(task)
                progress = True

    if not progress:
        break

print("EXECUTION ORDER:")
if len(execution_order) == 0:
    print("No task can be started.")
else:
    for i in range(len(execution_order)):
        print(f"Step {i + 1}: {execution_order[i]}")

if len(completed) == len(tasks):
    print("ALL TASKS COMPLETED SUCCESSFULLY")
else:
    print("ERROR: Circular dependency detected!")
    print("These tasks could not be completed:")
    for task in tasks:
        if task not in completed:
            print(task)