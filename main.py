from storage import load_tasks, save_tasks
from models import Task


def show_menu():
    print("1. Добавить задачу \n2. Показать все задачи \n3. Удалить задачу \n4. Выход")
    choice = input("Выберите операцию: ")
    return choice


def add_task():
    t = input("Ваша задача: ")
    p = input("Приоритет задачи: ")
    tasks = load_tasks()
    task = Task(id=len(tasks) + 1, text=t, priority=p)
    tasks.append(task)
    save_tasks(tasks)


def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    for v in tasks:
        print(v)


def delete_task():
    show_tasks()
    id = int(input("Введите id задачи чтобы ее удалить: "))
    tasks = load_tasks()
    tasks = [task for task in tasks if task.id != id]
    save_tasks(tasks)


while True:
    choice = show_menu()
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
