from storage import load_tasks, save_tasks


def show_menu():
    print("1. Добавить задачу \n2. Показать все задачи \n3. Удалить задачу \n4. Выход")
    choice = input("Выберите операцию: ")
    return choice


def add_task():
    t = input("Ваша задача: ")
    p = input("Приоритет задачи: ")
    task = {"text": t, "priority": p, "id": 1, "done": False}
    data = load_tasks()
    data["tasks"].append(task)
    save_tasks(data["tasks"])


def show_tasks():
    for v in load_tasks()["tasks"]:
        print(v)


def delete_task():
    show_tasks()
    id = int(input("Введите id задачи чтобы ее удалить: "))
    data = load_tasks()
    tasks = data["tasks"]
    tasks = [task for task in tasks if task["id"] != id]
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
